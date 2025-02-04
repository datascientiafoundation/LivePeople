---
title: FAQ
layout: base
permalink: /faq/
---

# FAQ

The DataScientia team is at your disposal for any questions related to technical aspects, clarifications or possible collaborations. [Contact Us](https://datascientia.disi.unitn.it/contact/).

1. [Data catalog search and navigation](#1-data-catalog-search-and-navigation)
2. [Data request, download and usage](#2-data-request-download-and-usage)
3. [Data upload and custom catalog](#3-data-upload-and-custom-catalog)


## 1. Data catalog search and navigation


#### What is the LivePeople catalog?

It is a data catalog allowing data consumers to discover which data are available and understand if it fits their purposes. Each dataset is described by:

- _[metadata]({{ site.baseurl }}/metadata)_ describes the data and the project that generated it;
- _documentation_ details the project and the data;
- _codebook_ shows data descriptive statistics for each dataset variable.

#### What is Datascientia?

You can find who we are on the [Datascientia webpage](https://datascientia.disi.unitn.it/about-us/).

#### Why are you not distributing your data through one of the existing data catalogs?

Current data catalogs are not designed to distribute person-centric data at our granularity level, thus requiring custom procedures. To reduce the risk of re-identification or abuse, the data are shared only for research purposes with identified researchers. The current procedure has been designed with legal and privacy experts.


#### What is the difference between datasets, bundles and projects?

- _Datasets_ are the basic units which contain the data from a single measurement instrument, such as accelerometer or step counter (e.g., 2018-SU2-Trento-Accelerometer). The name format is `<year>-<acronym for the data collection experiment>-<data collection location-dataset name>` of the sensor or measure instrument>.
- _Bundles_ are groups of datasets that can be classified as part of the same category or that are typically used together. For example, 2018-SU2-Trento-Connectivity groups Bluetooth, WiFi and cellular networks. The bundle metadata lists the contained datasets.
- _Project_ is a data collection study carried out in one location, such as 2018-Smart Unitn 2-Trento. It contains all the datasets collected during the study.

All these three types can be requested. Selecting a bundle or a project means that all the datasets that are contained are also selected.

#### Why are the datasets organized into datasets, bundles and projects?

Based on the GDPR minimization principle, data must be adequate, limited, and relevant for the analysis.  Thus, data from measurement instruments, such as accelerometer and time diaries, are provided separately. Researchers can request access to a single dataset of a specific data collection (e.g., WiFi networks in Italy in the DiversityOne data collection) or a combination of datasets from multiple data collection or sensors. To streamline dataset selection and download, we have created thematic bundles that group data commonly used together for key research purposes. For instance, activity recognition studies can download the motion bundle grouping accelerometer, activities, step counter and others. Another bundle is tailored for studying social interaction and combines questionnaires, time diaries, and location data. The catalog lists both bundles and datasets containing one single sensor.

#### What is the meaning of the metadata?

The metadata provides information about the dataset and allows the data consumers to understand whether it fits their needs or research questions. The [metadata glossary]({{ site.baseurl }}/metadata) describes them.

#### What is the Parquet format?

The format of each file in the datasets is [Apache Parquet](https://parquet.apache.org/), an efficient data storage format that can be opened by most of the existing data processing tools. Suggested tools: the Python library pandas `pd.read_parquet('path/to/dataset.parquet')`, [DuckDB](https://duckdb.org/), a in-process database solution,  [Tad](https://www.tadviewer.com/), a desktop application to visualize parquet files.



---



## 2. Data request, download and usage


#### Can I download the data directly from the data catalog?

No, data are not directly accessible from the data catalog. Each dataset webpage has a link to the request forms. LivePeople catalog provides access to the metadata only.

#### How to download the data?

After submitting the form online, if the request is accepted, you will receive an email with instructions on how to access the storage with the requested datasets. Access will be granted for a limited period.

#### Can I request the data from multiple data collection projects?

Yes, in the request form, you can request data from multiple projects.

#### Can I request all the data of a project?

Yes, Datascientia will evaluate the coherence of the research proposal with the requested datasets.

#### What are the eligibility criteria to request the data?

The specific criteria for each dataset are listed in the license. For most of the dataset, the main requirement is to be a researcher affiliated with a research institution, and the usage of the data is restricted to research purposes.

#### Can I also use the same data for another project besides the approved one?

No, a new dataset request or an update of the previous project proposal is needed.

#### Can I redistribute or transfer the downloaded datasets or their derived datasets to third parties?

The research entity can't, directly or indirectly, sell, license or sub-license, rent or otherwise transfer to third parties the dataset provided by this catalog, nor permit any third party to do so. Specific datasets may have different policies, please look at the use terms and license linked in the metadata in each dataset webpage.

#### Can I keep the data after the end of my research project?

No, the research entity that requested the data deletes it at the end date specified in the research proposal. The research entity is asked to notify the elimination.


---


## 3. Data upload and custom catalog

You can upload your [metadata values](({{ site.baseurl }}/metadata)) and/or your data to our catalog. 


#### Why should I create my catalog?

You can create your own instance of the catalog to redistribute data that you own. This will allow you to join the Datascientia network and increase the visibility of your data. [Contact us](https://datascientia.disi.unitn.it/contact/) if you have additional questions or if you want to join the community.

#### How can I create my own data catalog?

[DataScientia foundation](https://datascientia.eu/) provides a data catalog template, built on top of [JKAN](https://jkan.io/), which can be customized to your needs. [Contact DataScientia](https://datascientia.disi.unitn.it/contact/) to get the template, and become part of the community with your catalog.

#### Why should I upload my metadata and/or data on your catalog?

This allows you to make your data more visible and, if you want, leverage our data distribution procedure.

#### How can I upload my own data?

[Contact](https://datascientia.disi.unitn.it/contact/) us and we will provide the detailed steps. In summary, you need to provide the metadata values, data documentation, license, and how interested data consumers can download the data.

#### Can I organize a data collection using your infrastructure and/or services?
Yes, we support you in designing the study and provide access to our services. [Contact us](https://datascientia.disi.unitn.it/contact/) and describe what study you would like to organize.

