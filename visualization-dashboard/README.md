# Visualization Dashboards for Population-level Data

<!-- **HCLS customers are constantly striving to find ways of improving clinical health outcomes of a defined group of individuals for Population Health Management(PHM). Possessing and analyzing data allows providers to identify the greatest needs of the patient population. For example, if the majority of a patient population is suffering from a particular disease, say diabetes, obesity and also the corresponding social determinants of health. PHM allows providers to predict and identify patients at risk for hospital admissions, allows providers to create patient-specific care plans, and helps providers understand their patient population health trends.** -->


This dashboard, built with Amazon QuickSight, offers an interactive visual interface to help users (eg. clinicians, bioinformaticians, radiologists) get domain-specific view of patients at the population or cohort-level. It includes the following sheets:**

* Clinical Analysis - Provides an overview of clinical data at the population level
* Genomic Analysis - PProvides an overview of genomic data at the population level
* Imaging Analysis - Provides an overview of medical imaging data at the population level


## Visualization Dashboard for Patient-level Data

<!-- **HCLS customers are seeing a rapid growth in patient-level data size and diversity, that include genomic, clinical, medical imaging, medical claims, and sensor data. While multimodal data offers a comprehensive view that can improve patient outcomes and care, analyzing multiple modalities at scale is challenging, preventing customers from adopting multimodal analytics for precision health applications.** -->


This dashboard, built with Amazon QuickSight, offers a single, interactive visual interface to help users (eg. clinicians) get a complete view of a patient across multiple data modalities (clinical, genomic and imaging). To use this dashboard, simply select the Patient ID of interest using the menu located at the top-right of the dashboard. This will generate visulaizations across multiple data types, filtered for the selected patient.


## Amazon Quicksight Q:

Both the dashboards are enabled with [Q topic](https://docs.aws.amazon.com/quicksight/latest/user/working-with-quicksight-q.html), which allows users to ask natural language-based questions and receive answers with relevant visualizations that help them gain insights from the data.


<sub>To try Q, type your question in the search bar at the top of the dashboard. 
For example: Count of distinct patientid accross diffrent diagnosis description </sub>