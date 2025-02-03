---
title: FAQ
layout: faq
permalink: /faq/
---

# FAQ

The DataScientia team is at your disposal for any questions related to technical aspects, clarifications or possible collaborations. [Contact Us](https://datascientia.disi.unitn.it/contact/).

1. [Data catalog search and navigation](#1-data-catalog-search-and-navigation)
2. [Data request, download and usage](#2-data-request-download-and-usage)
3. [Data upload and custom catalog](#3-data-upload-and-custom-catalog)


## 1. Data catalog search and navigation

<details>
<summary>### What is the LivePeople catalog?</summary>

It is a data catalog allowing data consumers to discover which data are available and understand if it fits their purposes. Each dataset is described by:

- _[metadata](({{ site.baseurl }}/metadata))_ describes the data and the project that generated it;
- _documentation_ details the project and the data;
- _codebook_ shows data descriptive statistics for each dataset variable.
</details>

<details>
<summary>### What is Datascientia?</summary>

You can find who we are on the [Datascientia webpage](https://datascientia.disi.unitn.it/about-us/).
</details>

<details>
<summary>### Why are you not distributing your data through one of the existing data catalogs?</summary>

Current data catalogs are not designed to distribute person-centric data at our granularity level, thus requiring custom procedures. To reduce the risk of re-identification or abuse, the data are shared only for research purposes with identified researchers. The current procedure has been designed with legal and privacy experts.
</details>

<details>
<summary>### What is the difference between datasets, bundles and projects?</summary>

- _Datasets_ are the basic units which contain the data from a single measurement instrument, such as accelerometer or step counter (e.g., 2018-SU2-Trento-Accelerometer). The name format is `<year>-<acronym for the data collection experiment>-<data collection location-dataset name>` of the sensor or measure instrument>.
- _Bundles_ are groups of datasets that can be classified as part of the same category or that are typically used together. For example, 2018-SU2-Trento-Connectivity groups Bluetooth, WiFi and cellular networks. The bundle metadata lists the contained datasets.
- _Project_ is a data collection study carried out in one location, such as 2018-Smart Unitn 2-Trento. It contains all the datasets collected during the study.

All these three types can be requested. Selecting a bundle or a project means that all the datasets that are contained are also selected.
</details>

<details>
<summary>### Why are the datasets organized into datasets, bundles and projects?</summary>

Based on the GDPR minimization principle, data must be adequate, limited, and relevant for the analysis.  Thus, data from measurement instruments, such as accelerometer and time diaries, are provided separately. Researchers can request access to a single dataset of a specific data collection (e.g., WiFi networks in Italy in the DiversityOne data collection) or a combination of datasets from multiple data collection or sensors. To streamline dataset selection and download, we have created thematic bundles that group data commonly used together for key research purposes. For instance, activity recognition studies can download the motion bundle grouping accelerometer, activities, step counter and others. Another bundle is tailored for studying social interaction and combines questionnaires, time diaries, and location data. The catalog lists both bundles and datasets containing one single sensor.
</details>

<details>
<summary>### What is the meaning of the metadata?</summary>

The metadata provides information about the dataset and allows the data consumers to understand whether it fits their needs or research questions. The [metadata glossary]({{ site.baseurl }}/metadata) describes them.
</details>

<details>
<summary>### What is the Parquet format?</summary>

The format of each file in the datasets is [Apache Parquet](https://parquet.apache.org/), an efficient data storage format that can be opened by most of the existing data processing tools. Suggested tools: the Python library pandas `pd.read_parquet('path/to/dataset.parquet')`, [DuckDB](https://duckdb.org/), a in-process database solution,  [Tad](https://www.tadviewer.com/), a desktop application to visualize parquet files.
</details>


---



## 2. Data request, download and usage

<details>
<summary>### Can I download the data directly from the data catalog?</summary>

No, data are not directly accessible from the data catalog. Each dataset webpage has a link to the request forms. LivePeople catalog provides access to the metadata only.
</details>

<details>
<summary>### How to download the data?</summary>

After submitting the form online, if the request is accepted, you will receive an email with instructions on how to access the storage with the requested datasets. Access will be granted for a limited period.
</details>

<details>
<summary>### Can I request the data from multiple data collection projects?</summary>

Yes, in the request form, you can request data from multiple projects.
</details>

<details>
<summary>### Can I request all the data of a project?</summary>

Yes, Datascientia will evaluate the coherence of the research proposal with the requested datasets.

<details>
<summary>### What are the eligibility criteria to request the data?</summary>

The specific criteria for each dataset are listed in the license. For most of the dataset, the main requirement is to be a researcher affiliated with a research institution, and the usage of the data is restricted to research purposes.
</details>

<details>
<summary>### Can I also use the same data for another project besides the approved one?</summary>

No, a new dataset request or an update of the previous project proposal is needed.

<details>
<summary>### Can I redistribute or transfer the downloaded datasets or their derived datasets to third parties?</summary>

The research entity can't, directly or indirectly, sell, license or sub-license, rent or otherwise transfer to third parties the dataset provided by this catalog, nor permit any third party to do so. Specific datasets may have different policies, please look at the use terms and license linked in the metadata in each dataset webpage.
</details>

<details>
<summary>### Can I keep the data after the end of my research project?</summary>

No, the research entity that requested the data deletes it at the end date specified in the research proposal. The research entity is asked to notify the elimination.
</details>

---


## 3. Data upload and custom catalog

You can upload your [metadata values](({{ site.baseurl }}/metadata)) and/or your data to our catalog. 

<details>
<summary>### Why should I create my catalog?</summary>

You can create your own instance of the catalog to redistribute data that you own. This will allow you to join the Datascientia network and increase the visibility of your data. [Contact us](https://datascientia.disi.unitn.it/contact/) if you have additional questions or if you want to join the community.
</details>

<details>
<summary>### How can I create my own data catalog?</summary>

[DataScientia foundation](https://datascientia.eu/) provides a data catalog template, built on top of [JKAN](https://jkan.io/), which can be customized to your needs. [Contact DataScientia](https://datascientia.disi.unitn.it/contact/) to get the template, and become part of the community with your catalog.
</details>

<details>
<summary>### Why should I upload my metadata and/or data on your catalog?</summary>

This allows you to make your data more visible and, if you want, leverage our data distribution procedure.
</details>

<details>
<summary>### How can I upload my own data?</summary>

[Contact](https://datascientia.disi.unitn.it/contact/) us and we will provide the detailed steps. In summary, you need to provide the metadata values, data documentation, license, and how interested data consumers can download the data.
</details>

<details>
<summary>### Can I organize a data collection using your infrastructure and/or services?</summary>
Yes, we support you in designing the study and provide access to our services. [Contact us](https://datascientia.disi.unitn.it/contact/) and describe what study you would like to organize.
</details>
