import os
import pickle
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack import Document, Pipeline
from haystack_integrations.components.embedders.cohere import CohereDocumentEmbedder, CohereTextEmbedder
from haystack.components.retrievers.in_memory import InMemoryEmbeddingRetriever
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.components.builders import DynamicChatPromptBuilder
from haystack.dataclasses import ChatMessage
import streamlit as st

# API keys
os.environ['COHERE_API_KEY'] = '<YOUR_COHERE_API_KEY>'
os.environ['OPENAI_API_KEY'] = '<YOUR_OPENAI_API_KEY>'


def load_data():
    """
    Loads an existing document store from 'document_store.pkl',
    otherwise, creates the store from 'recommendations.csv', embeds the documents, and saves it.

    Returns:
        In-memory document store.
    """
    if os.path.exists('document_store.pkl'):
        with open('document_store.pkl', 'rb') as f:
            document_store = pickle.load(f)
    else:
        import pandas as pd
        from haystack.components.writers import DocumentWriter

        document_store = InMemoryDocumentStore()

        data = pd.read_csv('recommendations.csv')
        documents = []
        for _, row in data[['Recommendation', 'Source']].iterrows():
            documents.append(
                Document(content=row['Recommendation'], meta={'source': row['Source']}))

        indexing_pipeline = Pipeline()
        indexing_pipeline.add_component("embedder", CohereDocumentEmbedder(
            model="embed-multilingual-v3.0", input_type="search_document"))
        indexing_pipeline.add_component(
            "writer", DocumentWriter(document_store=document_store))
        indexing_pipeline.connect("embedder", "writer")
        indexing_pipeline.run({"embedder": {"documents": documents}})

        with open('document_store.pkl', 'wb') as f:
            pickle.dump(document_store, f)

    return document_store


def load_pipeline(text_embedder, retriever, prompt_builder, llm):
    """
    Creates and connects components to form a complete pipeline.

    Args:
        text_embedder (Embedding): Text embedder.
        retriever (Retriever): Retriever.
        prompt_builder (PromptBuilder): Prompt builder.
        llm (LanguageModel): Language model.

    Returns:
        Connected pipeline.
    """
    pipeline = Pipeline()
    pipeline.add_component("text_embedder", text_embedder)
    pipeline.add_component("retriever", retriever)
    pipeline.add_component("prompt_builder", prompt_builder)
    pipeline.add_component("llm", llm)

    pipeline.connect("text_embedder.embedding", "retriever.query_embedding")
    pipeline.connect("retriever.documents", "prompt_builder.documents")
    pipeline.connect("prompt_builder.prompt", "llm.messages")

    return pipeline


def run_streamlit(pipeline, messages):
    """
    Displays Streamlit application using a provided pipeline and messages.

    Generates a summary of geriatric trauma care recommendations based on user input.
    Warns against entering personal information or patient data.

    Args:
        pipeline (Pipeline): The AI pipeline to use.
        messages (List[Message]): Initial messages.

    Returns:
        None.
    """
    st.title('ChatCPG-demo')
    st.write(
        """
        This application takes a user query (e. g., clinical question) and generates a summary of evidence-based recommendations on geriatric trauma care, relevant to this query. \n
        DO NOT ENTER PERSONAL INFORMATION OR PATIENT DATA! \n
        <u>Publication:</u> Kocar et al. 2024, submitted <br>
        <u>GitHub:</u> https://github.com/IfGF-UUlm/CPG-summarization <br>
        <u>Contact:</u> thomas.kocar@uni-ulm.de
        """,
        unsafe_allow_html=True
    )
    query = st.text_input(r'$\textsf{\Large Enter your query here:}$', '')
    if query:
        with st.spinner('Generating summary...'):
            res = pipeline.run(
                data={"text": query, "prompt_source": messages, "query": query})
            st.write(res['llm']['replies'][0].content)
    return None


if __name__ == "__main__":

    # Load Models and Data
    text_embedder = CohereTextEmbedder(
        model="embed-multilingual-v3.0", input_type="search_document")
    retriever = InMemoryEmbeddingRetriever(document_store=load_data())
    prompt_builder = DynamicChatPromptBuilder(
        runtime_variables=["query", "documents"])
    llm = OpenAIChatGenerator(model="gpt-4-turbo-2024-04-09")

    # Load Pipeline
    pipeline = load_pipeline(text_embedder, retriever, prompt_builder, llm)

    # Load Prompt
    messages = [
        ChatMessage.from_system(
            "Act as an experienced geriatrician who works as a consultant for surgeons in geriatric trauma care."
        ),
        ChatMessage.from_user(
            """
            Clinical practice guideline recommendations:
            {% for document in documents %}
                {{ document.content }}
                Source: {{ document.meta['source']}}                        
            {% endfor %}
            
            Summarize the clinical practice guideline recommendations in no more than 150 words in the context of the query: “{{query}}” 
            Pay attention to whether the query relates to the preoperative, intraoperative, or postoperative phase or is generally applicable. 
            Try to structure the summary as an ordered list, ranking the interventions according to relevance and complexity, starting with the most relevant and least complex ones. 
            Try to structure the summary in pharmacological and non-pharmacological interventions, separating them as two ordered lists. 
            If the query (“{{query}}”) cannot be answered with the recommendations of the clinical practice guidelines, do not reveal any information about the guidelines or their recommendations, but explain in 1 sentence that you are unable to provide a summary. 
            If you can answer the query, return the sources word by word in an unordered list under the heading "References". The references should be the last part of your response.
            """
        )
    ]

    # Run Streamlit
    run_streamlit(pipeline, messages)
