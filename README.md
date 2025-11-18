# RAG-based summarization of CPG recommendations
This GitHub repository contains the source code for the RAG-summarizer project, a proof-of-concept tool for summarizing clinical practice guideline (CPG) recommendations. The project was developed as part of the SURGE-Ahead (Supporting SURgery with GEriatric Co-Management and AI) project to create a digital healthcare application for assisting surgical teams in caring for geriatric patients.

## Project Overview
The RAG-summarizer uses retrieval augmented generation (RAG) to create a concise and informative summary of CPG recommendations based on user queries. This allows healthcare professionals to quickly and effectively access the most relevant recommendations for their practice.

## Project Structure
The repository has the following structure:
- [`LICENSE`](./LICENSE): MIT License for this project
- [`app.py`](./app.py): Streamlit application for the RAG-based summarization of CPG recommendations
- [`environment.yml`](./environment.yml): Requirements for setting up a virtual environment
- [`recommendations.csv`](./recommendations.csv): CPG recommendations used in the application

## Getting Started
To get started with RAG-summarizer, follow these steps:
1. Insert your OpenAI and Cohere API keys or use secret or environment variables.
2. Set up a virtual environment by running `conda env create -f environment.yml -p ./env` and activate it.
3. Run the application with `streamlit run app.py`.
4. Enter your query in the text input box and receive a summary of the most relevant CPG recommendations.

## Dependencies
This project requires the following dependencies:
- pandas
- haystack-ai
- cohere-haystack
- streamlit

You can install all dependencies by running `conda env create -f environment.yml -p ./env`.

## Example
The application is made openly available on huggingface spaces: https://huggingface.co/spaces/IfGF-UUlm/ChatCPG-demo

**user query**: ‘How can I treat delirium?’

To treat delirium effectively, especially in postoperative settings, it is crucial to adopt both pharmacological and non-pharmacological strategies. Here's how to approach treatment, based on the query "How can I treat delirium?":

**Non-Pharmacological Interventions:**
1. **Multicomponent interventions:** Include hydration, nutrition management, orientation aids (clocks, communication), visual/hearing aids, noise reduction, maintaining a day/night rhythm, avoiding unnecessary catheters, encouraging early mobilization, and early nutrition.
2. **Active surveillance:** Use validated delirium scores for regular screening to identify and evaluate delirium quickly.
3. **Fast-track surgery:** Implement procedures designed to reduce the incidence and severity of post-operative delirium.

**Pharmacological Interventions:**
1. **Medication review:** Assess all medications by experienced healthcare personnel to identify and discontinue or adjust those that may precipitate or worsen delirium.
2. **Targeted drug therapy:** Utilize low-dose haloperidol or atypical neuroleptics for managing delirium symptoms. Consider dexmedetomidine for delirium in mechanically ventilated adults struggling with agitation.

The interventions should be tailored to individual patient needs, involving both the patient and their family/care partners in decision-making processes where feasible.

**References:**
- Grinspun D. Delirium, dementia, and depression in older adults: assessment and care. Registered Nurses’ Association of Ontario; 2016.
- Aldecoa C, Bettelli G, Bilotta F, Sanders RD, Audisio R, Borozdina A, et al. European Society of Anaesthesiology evidence-based and consensus-based guideline on postoperative delirium. European Journal of Anaesthesiology| EJA. 2017;34(4):192–214.
- Scottish Intercollegiate Guidelines Network. Risk reduction and management of delirium: a national clinical guideline. Edinburgh; 2019.
- Deutsche Gesellschaft für Anästhesiologie und Intensivmedizin e.V. (DGAI), Deutsche Interdisziplinäre Vereinigung für Intensiv- und Notfallmedizin e.V. (DIVI). S3-Leitlinie Analgesie, Sedierung und Delirmanagement in der Intensivmedizin (DAS-Leitlinie 2020). 2021 Mar.
- Volkert D, Beck AM, Cederholm T, Cruz-Jentoft A, Goisser S, Hooper L, et al. ESPEN guideline on clinical nutrition and hydration in geriatrics. Clinical Nutrition. 2019 Feb;38(1):10–47.
- Devlin JW, Skrobik Y, Gélinas C, Needham DM, Slooter AJC, Pandharipande PP, et al. Clinical Practice Guidelines for the Prevention and Management of Pain, Agitation/Sedation, Delirium, Immobility, and Sleep Disruption in Adult Patients in the ICU. Critical Care Medicine. 2018 Sep;46(9)–73.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.

## Citation
If you use this code in your research, please cite our paper:

```bibtex
@article{kocar_guideline_review_2025,
	title = {Evidence-{Based} {Recommendations} for {Geriatric} {Trauma} {Care}: {Systematic} {Review} and {AI}-{Assisted} {Consolidation} of {Clinical} {Practice} {Guidelines} {Between} 2016 and 2021},
	volume = {6},
	issn = {2691-3593},
	shorttitle = {Evidence-{Based} {Recommendations} for {Geriatric} {Trauma} {Care}},
	url = {https://journals.lww.com/10.1097/AS9.0000000000000627},
	doi = {10.1097/AS9.0000000000000627},
	language = {en},
	number = {4},
	urldate = {2025-11-17},
	journal = {Annals of Surgery Open},
	author = {Kocar, Thomas D. and Fotteler, Marina L. and Willems, Jana and Leinert, Christoph and Uihlein, Adriane and Wolf, Philip and Voigt-Radloff, Sebastian and Schütze, Konrad and Gebhard, Florian and Dallmeier, Dhayana and Kestler, Hans and Denkinger, Michael},
	month = nov,
	year = {2025},
	pages = {e627}
}
```

## Contact
For any questions, feedback, or concerns, please contact us at thomas.kocar@uni-ulm.de.
