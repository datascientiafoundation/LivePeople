---
title: metadata
layout: base
permalink: /metadata/
---

| Field Name       | Description                                        |
|------------------|----------------------------------------------------|
| **Project title** | name of the DataScientia project in a natural language as a string |
| **Project url** | this attribute encodes the dereferenciable URL of the DataScientia project |
| **Project webpage** | this attribute encodes the dereferenciable URL of the DataScientia project |
| **Project keywords** | list of keywords in a natural language to quickly understand the theme of the project |
| **Project type** | the type of the DataScientia project. e.g., Knowledge Resource Generation, Knowledge Resource Annotation, etc |
| **Project description** | description of the DataScientia project in a natural language, namely (i) the project name and objectives; (ii) the type of data collected; (iii) suggested reuse. |
| **Project start datae** | the date of the commencement of a DataScientia project |
| **Project end datae** | the date of conclusion of a DataScientia project |
| **Project funding agency** | the name of the agency or institution funding a DataScientia project and, if available, the grant agreement number. European projects also have a DOI, e.g., https://doi.org/10.3030/823783  |
| **Project input** | this (repeatable) attribute encodes the various inputs (e.g., datasets, specifications, etc.) with respect to a DataScientia project. |
| **Project output** | this (repeatable) attribute encodes the various outputs (e.g., datasets, domain languages, etc.) with respect to a DataScientia project. |
| **Project coordinator** | the name of the research coordinator in charge of a DataScientia project |
| **Project observations** | this attribute can be used to record any observations about a DataScientia project in a natural language. |
| **Project coordinator organization** | Institution of the ds:prjCoordinator |
| **Project project area** | Category of the project that pertains to the Catalog (LivePeople, LiveLanguage, LiveKnowledge, LiveData, LiveMedia). |
| **Project members** | Other members who took part in the project with roles other than the coordinator |
| **Project target location** | expected project data collection area |
| **Project target population** | Sociodemographic characteristics that were adopted as population inclusion criteria (e.g. gender, age, educational qualification, profession). Multiple options can be selected |
| **Project overall participants involved** | Total number of participants who were involved in the project |
| **Project selected participants** | Number of participants who have been selected for the project (less than or equal to ds:prjOverallPeopleInvolved), if the project has multiple phases |
| **Project type of measurements** | Survey methods that were used to collect participant data (i.e., Questionnaire, Structured Interview, Semi-Structured Interview, Participant Observation, Intensive Longitudinal Survey). Multiple options can be selected |
| **Project irbapproval datae** | Date of Institutional review board (IRB) approval of the project |
| **Project irbapproval organization** | Institution to which the committee belongs to |
| **Project irbapproval number** | Number of protocol of the approval |
| **Project cite as** | Bibtext citation of the project |
| **Project maintenance** | description of the dataset maintenance process: how often is the dataset updated, how updates will be communicated, who is responsible for the updates, whether and how older versions will be supported |
| **Project latitude** | Latitude of the centroid of ds:prjTargetLocation (maily for visualization purposes on the catalog website) |
| **Project longitude** | Longitude of the centroid of ds:prjTargetLocation (maily for visualization purposes on the catalog website) |
| **Project documentation name** | Project documentation name |
| **Project documentation url** | Project documentation URL |
| **Project documentation format** | Project documentation format |
| **Project additional material name** | Project additional material name |
| **Project additional material url** | Project additional material URL |
| **Project additional material format** | Project additional material format |
| **Data name** | the name of the dataset in a natural language |
| **Data description** | a description of the dataset |
| **Data version** | the version of the dataset. The schema to follow is MAJOR.MINOR.PATCH as described https://semver.org/spec/v2.0.0.html |
| **Data publication timestamp** | the timestamp of the publication of the dataset in the respective catalog. |
| **Data license** | license of the dataset |
| **Data url** | the dereferenceable URL of the dataset |
| **Data keyword** | the keywords which can quickly convey the topic of the dataset |
| **Data publisher** | the publisher of the dataset |
| **Data creator** | the creator of the dataset. Individual member of the community or organization. |
| **Data owner** | the owner of the dataset. Individual member of the community or organization. |
| **Data language** | The language of the dataset (only if dataset type==Synchronic interaction | dataset type==Diachronic interaction). Recommended values are taken from https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes. When not applicable use N/A |
| **Data level** | the knowledge level of the dataset, e.g., L1-2, L4 |
| **Data size** | the byte size of the dataset (e.g., the size of the file parquet) |
| **Data domain** | the domain to which the dataset belongs. Possible values are: Digital University, Territory & Society, Health |
| **Data file format** | type of the file using MIME format https://www.iana.org/assignments/media-types/media-types.xhtml |
| **Data detailed description** | links the dataset to its personalized project web page. Please note that is different from the ds:prjURL attribute, which links to the datascientia project on the community. |
| **Data download request** | email of the institution responsible for validating the download request and share the data or link to the form to fill |
| **Data conditions of access** | conditions that affect the availability of the data. E.g., only for scientific purposes |
| **Data genre** | Genre of the dataset: images, tabular data, geographical file |
| **Datais accessible for free** | nan |
| **Data expires** | When the dataset is no longer available  |
| **Data type** | The type of dataset |
| **Data sensor type** | The type of sensor (only if dataset type == Sensor) |
| **Data start datae** | The begin of the data collection (i.e., the oldest date in the dataset) |
| **Data end datae** | The end of the data collection (i.e., the most recent date in the dataset) |
| **Data five stars** | Ranking based on Tim Berners-Lee's 5-star deployment scheme for Open Data (https://5stardata.info/en/). iLog data after the data preparation are 3 stars |
| **Data origin** | Origin of the data. Synthetic: generated from an algorithm. Direct observation: collected from humans through human behavior studies. Composition: dataset resulting from the composition of other datasets. Feature engineering: dataset as the result of features extraction or aggregation of existing datasets; |
| **Data creative work status** | Status of the data. Raw: no preprocessing has been performed. Cleaned: cleaning procedures has been applied to the raw data. Reduced: the data has been aggregated, e.g., to generate features. Enriched: contains additional data from third parties. |
| **Data download request name** | The name of the document to request the dataset |
| **Data download request url** | The link to the downloadable document to request the dataset |
| **Data download request format** | The format of the resource |
| **Data documentation name** | link to the dataset documentation, e.g., techinical report describing the data collection (design, collection, preparation, main results) |
| **Data documentation url** | The link to the downloadable documentation |
| **Data documentation format** | The format of the resource |
| **Data additional material name** | link to the materials used during the research (e.g., focus group tracks, interviews, and questionnaires) |
| **Data additional material url** | The link to the downloadable additional material |
| **Data additional material format** | The format of the resource |
| **Data codebook name** | A codebook describes the contents of a data collection. A well-documented code- book contains information intended to be complete and self-explanatory for each variable in a dataset. |
| **Data codebook url** | The link to the downloadable codebook |
| **Data codebook format** | The format of the resource |
| **Data identifier** | alpha numeric code identifing the resource (see Identifier sheet) |
| **Data changelog url** | nan |
| **Data licence url** | nan |
| **Data sha256** | hash of the content of the file |
| **Data update timestamp** | last date the dataset has been updated |
| **Data based on** | A resource from which this work is derived or from which it is a modification or adaptation. It is a link to Dataset, Project, Url |
| **Data sensor name** | single sensor name  |
