---
title: metadata
layout: base
permalink: /metadata/
---

| Field Name       | Description                                        |
|------------------|----------------------------------------------------|
| **Project&nbsp;title** | name of the DataScientia project in a natural language as a string |
| **Project&nbsp;url** | this attribute encodes the dereferenciable URL of the DataScientia project |
| **Project&nbsp;webpage** | this attribute encodes the dereferenciable URL of the DataScientia project |
| **Project&nbsp;keywords** | list of keywords in a natural language to quickly understand the theme of the project |
| **Project&nbsp;type** | the type of the DataScientia project. e.g., Knowledge Resource Generation, Knowledge Resource Annotation, etc |
| **Project&nbsp;description** | description of the DataScientia project in a natural language, namely (i) the project name and objectives; (ii) the type of data collected; (iii) suggested reuse. |
| **Project&nbsp;start&nbsp;date** | the date of the commencement of a DataScientia project |
| **Project&nbsp;end&nbsp;date** | the date of conclusion of a DataScientia project |
| **Project&nbsp;funding&nbsp;agency** | the name of the agency or institution funding a DataScientia project and, if available, the grant agreement number. European projects also have a DOI, e.g., https://doi.org/10.3030/823783  |
| **Project&nbsp;input** | this (repeatable) attribute encodes the various inputs (e.g., datasets, specifications, etc.) with respect to a DataScientia project. |
| **Project&nbsp;output** | this (repeatable) attribute encodes the various outputs (e.g., datasets, domain languages, etc.) with respect to a DataScientia project. |
| **Project&nbsp;coordinator** | the name of the research coordinator in charge of a DataScientia project |
| **Project&nbsp;observations** | this attribute can be used to record any observations about a DataScientia project in a natural language. |
| **Project&nbsp;coordinator&nbsp;organization** | Institution of the ds:prjCoordinator |
| **Project&nbsp;project&nbsp;area** | Category of the project that pertains to the Catalog (LivePeople, LiveLanguage, LiveKnowledge, LiveData, LiveMedia). |
| **Project&nbsp;members** | Other members who took part in the project with roles other than the coordinator |
| **Project&nbsp;target&nbsp;location** | expected project data collection area |
| **Project&nbsp;target&nbsp;population** | Sociodemographic characteristics that were adopted as population inclusion criteria (e.g. gender, age, educational qualification, profession). Multiple options can be selected |
| **Project&nbsp;overall&nbsp;participants&nbsp;involved** | Total number of participants who were involved in the project |
| **Project&nbsp;selected&nbsp;participants** | Number of participants who have been selected for the project (less than or equal to ds:prjOverallPeopleInvolved), if the project has multiple phases |
| **Project&nbsp;type&nbsp;of&nbsp;measurements** | Survey methods that were used to collect participant data (i.e., Questionnaire, Structured Interview, Semi-Structured Interview, Participant Observation, Intensive Longitudinal Survey). Multiple options can be selected |
| **Project&nbsp;IRB&nbsp;approval&nbsp;date** | Date of Institutional review board (IRB) approval of the project |
| **Project&nbsp;IRB&nbsp;approval&nbsp;organization** | Institution to which the committee belongs to |
| **Project&nbsp;IRB&nbsp;approval&nbsp;number** | Number of protocol of the approval |
| **Project&nbsp;cite&nbsp;as** | Bibtext citation of the project |
| **Project&nbsp;maintenance** | description of the dataset maintenance process: how often is the dataset updated, how updates will be communicated, who is responsible for the updates, whether and how older versions will be supported |
| **Project&nbsp;latitude** | Latitude of the centroid of ds:prjTargetLocation (maily for visualization purposes on the catalog website) |
| **Project&nbsp;longitude** | Longitude of the centroid of ds:prjTargetLocation (maily for visualization purposes on the catalog website) |
| **Project&nbsp;documentation&nbsp;name** | Project documentation name |
| **Project&nbsp;additional&nbsp;material&nbsp;name** | Project additional material name |
| **Data&nbsp;name** | the name of the dataset in a natural language |
| **Data&nbsp;description** | a description of the dataset |
| **Data&nbsp;version** | the version of the dataset. The schema to follow is MAJOR.MINOR.PATCH as described https://semver.org/spec/v2.0.0.html |
| **Data&nbsp;publication&nbsp;timestamp** | the timestamp of the publication of the dataset in the respective catalog. |
| **Data&nbsp;license** | license of the dataset |
| **Data&nbsp;url** | the dereferenceable URL of the dataset |
| **Data&nbsp;keyword** | the keywords which can quickly convey the topic of the dataset |
| **Data&nbsp;publisher** | the publisher of the dataset |
| **Data&nbsp;creator** | the creator of the dataset. Individual member of the community or organization. |
| **Data&nbsp;owner** | the owner of the dataset. Individual member of the community or organization. |
| **Data&nbsp;language** | The language of the dataset (only if dataset type==Synchronic interaction \| dataset type==Diachronic interaction). Recommended values are taken from https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes. When not applicable use N/A |
| **Data&nbsp;level** | the knowledge level of the dataset, e.g., L1-2, L4 |
| **Data&nbsp;size** | the byte size of the dataset (e.g., the size of the file parquet) |
| **Data&nbsp;domain** | the domain to which the dataset belongs. Possible values are: Digital University, Territory & Society, Health |
| **Data&nbsp;file&nbsp;format** | type of the file using MIME format https://www.iana.org/assignments/media-types/media-types.xhtml |
| **Data&nbsp;detailed&nbsp;description** | links the dataset to its personalized project web page. Please note that is different from the ds:prjURL attribute, which links to the datascientia project on the community. |
| **Data&nbsp;download&nbsp;request** | email of the institution responsible for validating the download request and share the data or link to the form to fill |
| **Data&nbsp;conditions&nbsp;of&nbsp;access** | conditions that affect the availability of the data. E.g., only for scientific purposes |
| **Data&nbsp;genre** | Genre of the dataset: images, tabular data, geographical file |
| **Data&nbsp;is&nbsp;accessible&nbsp;for&nbsp;free** |  |
| **Data&nbsp;expires** | When the dataset is no longer available  |
| **Data&nbsp;type** | The type of dataset |
| **Data&nbsp;sensor&nbsp;type** | The type of sensor (only if dataset type == Sensor) |
| **Data&nbsp;start&nbsp;date** | The begin of the data collection (i.e., the oldest date in the dataset) |
| **Data&nbsp;end&nbsp;date** | The end of the data collection (i.e., the most recent date in the dataset) |
| **Data&nbsp;five&nbsp;stars** | Ranking based on Tim Berners-Lee's 5-star deployment scheme for Open Data (https://5stardata.info/en/). iLog data after the data preparation are 3 stars |
| **Data&nbsp;origin** | Origin of the data. Synthetic: generated from an algorithm. Direct observation: collected from humans through human behavior studies. Composition: dataset resulting from the composition of other datasets. Feature engineering: dataset as the result of features extraction or aggregation of existing datasets; |
| **Data&nbsp;creative&nbsp;work&nbsp;status** | Status of the data. Raw: no preprocessing has been performed. Cleaned: cleaning procedures has been applied to the raw data. Reduced: the data has been aggregated, e.g., to generate features. Enriched: contains additional data from third parties. |
| **Data&nbsp;download&nbsp;request&nbsp;name** | The name of the document to request the dataset |
| **Data&nbsp;documentation&nbsp;name** | link to the dataset documentation, e.g., techinical report describing the data collection (design, collection, preparation, main results) |
| **Data&nbsp;additional&nbsp;material&nbsp;name** | link to the materials used during the research (e.g., focus group tracks, interviews, and questionnaires) |
| **Data&nbsp;codebook&nbsp;name** | A codebook describes the contents of a data collection. A well-documented code- book contains information intended to be complete and self-explanatory for each variable in a dataset. |
| **Data&nbsp;identifier** | alpha numeric code identifing the resource (see Identifier sheet) |
| **Data&nbsp;changelog&nbsp;url** |  |
| **Data&nbsp;licence&nbsp;url** |  |
| **Data&nbsp;sha256** | hash of the content of the file |
| **Data&nbsp;update&nbsp;timestamp** | last date the dataset has been updated |
| **Data&nbsp;based&nbsp;on** | A resource from which this work is derived or from which it is a modification or adaptation. It is a link to Dataset, Project, Url |
| **Data&nbsp;sensor&nbsp;name** | single sensor name  |
