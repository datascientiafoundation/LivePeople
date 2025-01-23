import pandas as pd
import os
import glob
import yaml
from dateutil import parser
import ast
import urllib.parse
import modeling as md

def convert_datetime_formats(date_value):
    # Parse date
    if isinstance(date_value, str):
        date_value = parser.parse(date_value)

    # Standardize date to "%Y-%m-%d %H:%M:%S"
    standardized_date = date_value.strftime("%Y-%m-%d %H:%M:%S")

    # Check if time is 00:00:00, remove the time if it's exactly at midnight
    if standardized_date.endswith(" 00:00:00"):
        standardized_date = standardized_date.split(" ")[0]

    return standardized_date


def encode_url(title):
    return urllib.parse.quote(title)


def generate_html_href(row, df):
    base_url = "https://datascientiafoundation.github.io/LivePeople/datasets/"
    generated_href = []

    if row['category'] == 'Project':  # Should contain Dataset Bundles
        titles = df[(df['category'] == 'Dataset Bundle') & (df['title'].str.startswith(row['title']))]['title']

        for title in titles:
            link = base_url + encode_url(title)
            label = '-'.join(title.split('-')[3:]).lower()
            generated_href.append(f'<a href="{link}">{label}</a>')

    elif row['category'] == 'Dataset Bundle':
        year_collection_city = '-'.join(row['title'].split('-')[0:3])
        bundle_name = '-'.join(row['title'].split('-')[3:])
        titles = df[(df['category'] == 'Dataset') & (df['title'].str.startswith(year_collection_city)) & (df[
                                                                                                              'sensor_type'] == bundle_name)][
            'title']

        for title in titles:
            link = base_url + encode_url(title)
            label = '-'.join(title.split('-')[3:]).lower()
            generated_href.append(f'<a href="{link}">{label}</a>')

    return ', '.join(generated_href)


def create_project_md(df):
    for index, row in df.iterrows():
        try:
            file_name = row['title']+'.md'

            for key in ["start_date", "end_date", "publication_date"]:
                row[key] = convert_datetime_formats(row[key])

            md_content = "---\n"

            md_content = md_content + "ds:prjTitle: " + row['title'] + "\n"
            md_content = md_content + "ds:prjURL: " + row['project_url'] + "\n"
            md_content = md_content + "ds:prjKeywords: " + row['schema'] + "\n"
            md_content = md_content + "ds:prjDescription: " + row['notes'] + "\n"
            md_content = md_content + "ds:prjStartDate: " + row['start_date'] + "\n"
            md_content = md_content + "ds:prjEndDate: " + row['end_date'] + "\n"
            md_content = md_content + "ds:prjFundingAgency: " + row['schema'] + "\n"
            md_content = md_content + "ds:prjInput: " + row['schema'] + "\n"
            md_content = md_content + "ds:prjOutput: " + row['schema'] + "\n"
            md_content = md_content + "ds:prjCoordinator: " + row['schema'] + "\n"
            md_content = md_content + "ds:prjObservations: " + row['schema'] + "\n"
            md_content = md_content + "ds:prjCoordinatorOrganization: " + row['organization'] + "\n"
            md_content = md_content + "ds:prjProjectArea: " + row['schema'] + "\n"
            md_content = md_content + "ds:prjMembers: " + row['schema'] + "\n"
            md_content = md_content + "ds:prjTargetLocation: " + row['location'] + "\n"
            md_content = md_content + "ds:prjTargetPopulation: " + row['schema'] + "\n"
            md_content = md_content + "ds:prjOverallParticipantsInvolved: " + row['schema'] + "\n"
            md_content = md_content + "ds:prjSelectedParticipants: " + row['number_participants'] + "\n"
            md_content = md_content + "ds:prjTypeOfMeasurements: " + row['schema'] + "\n"
            md_content = md_content + "ds:prjIRBApprovalDate: " + row['schema'] + "\n"
            md_content = md_content + "ds:prjIRBApprovalOrganization: " + row['schema'] + "\n"
            md_content = md_content + "ds:prjIRBApprovalNumber: " + row['schema'] + "\n"
            md_content = md_content + "ds:prjCiteAs: " + row['schema'] + "\n"
            md_content = md_content + "ds:prjMaintenance: " + row['schema'] + "\n"
            md_content = md_content + "ds:prjLatitude: " + row['latitude_map'] + "\n"
            md_content = md_content + "ds:prjLongitude: " + row['longitude_map'] + "\n"
            md_content = md_content + "ds:prjThumbnailUrl: " + row['schema'] + "\n"
            md_content = md_content + "ds:prjIdentifier: " + row['schema'] + "\n"
            md_content = md_content + "ds:prjDownloadRequestEmail: " + row['schema'] + "\n"
            md_content = md_content + "ds:prjDurationFacet: " + row['schema'] + "\n"
            md_content = md_content + "ds:prjLocationFacet: " + row['schema'] + "\n"
            md_content = md_content + "ds:prjCollectionFacet: " + row['schema'] + "\n"
            md_content = md_content + "ds:prjCategoryFacet: " + row['schema'] + "\n"

            md_content = md_content + "---\n"

            output_file_path = os.path.join(output_dir, file_name)

            with open(output_file_path, 'w', encoding='utf-8') as md_file:
                md_file.write(md_content)
        except Exception as e:
            print(f"Error processing file {row['title']}: {e}")

def create_dataset_md(df):
    for index, row in df.iterrows():
        try:
            file_name = row['title']+'.md'

            for key in ["start_date", "end_date", "publication_date"]:
                row[key] = convert_datetime_formats(row[key])

            md_content = "---\n"

            md_content = md_content + "ds:DatTitle: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatName: " + row['title'] + "\n"
            md_content = md_content + "ds:DatDescription: " + row['project_url'] + "\n"
            md_content = md_content + "ds:DatVersion: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatPublicationTimestamp: " + row['notes'] + "\n"
            md_content = md_content + "ds:DatLicense: " + row['start_date'] + "\n"
            md_content = md_content + "ds:DatURL: " + row['end_date'] + "\n"
            md_content = md_content + "ds:DatKeyword: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatPublisher: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatCreator: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatOwner: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatLanguage: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatLevel: " + row['organization'] + "\n"
            md_content = md_content + "ds:DatSize: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatDomain: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatFileFormat: " + row['location'] + "\n"
            md_content = md_content + "ds:DatDetailedDescription: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatDownloadRequest: " + row['number_participants'] + "\n"
            md_content = md_content + "ds:DatConditionsOfAccess: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatGenre: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatisAccessibleForFree: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatExpires: " + row['schema'] + "\n"

            md_content = md_content + "ds:DatType: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatSensorType: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatStartDate: " + row['latitude_map'] + "\n"
            md_content = md_content + "ds:DatEndDate: " + row['longitude_map'] + "\n"
            md_content = md_content + "ds:DatFiveStars: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatOrigin: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatCreativeWorkStatus: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatIdentifier: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatChangelogURL: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatLicenceURL: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatSha256: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatUpdateTimestamp: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatBasedOn: " + row['schema'] + "\n"

            md_content = md_content + "ds:DatSensorName: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatDurationFacet: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatLocationFacet: " + row['schema'] + "\n"
            md_content = md_content + "ds:DataTypeFacet: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatCategoryFacet: " + row['schema'] + "\n"

            md_content = md_content + "ds:DatLatitude: " + row['schema'] + "\n"
            md_content = md_content + "ds:DatLongitude: " + row['schema'] + "\n"

            md_content = md_content + "download request:\n"

            if str(row['ds:DatDownloadRequestName']) != "nan":
                md_content = md_content + "  - name: " + str(row['ds:DatDownloadRequestName']) + "\n"
                md_content = md_content + "    url: " + str(row['ds:DatDownloadRequestURL']) + "\n"
                md_content = md_content + "    format: " + str(row['ds:DatDownloadRequestFormat']) + "\n"

            md_content = md_content + "resources:\n"

            if str(row['ds:DatDocumentationName']) != "nan":
                md_content = md_content + "  - name: " + str(row['ds:DatDocumentationName']) + "\n"
                md_content = md_content + "    url: " + str(row['ds:DatDocumentationURL']) + "\n"
                md_content = md_content + "    format: " + str(row['ds:DatDocumentationFormat']) + "\n"

            if str(row['ds:DatCodebookName']) != "nan":
                md_content = md_content + "  - name: " + str(row['ds:DatCodebookName']) + "\n"
                md_content = md_content + "    url: " + str(row['ds:DatCodebookURL']) + "\n"
                md_content = md_content + "    format: " + str(row['ds:DatCodebookFormat']) + "\n"

            if str(row['ds:DatAdditionalMaterialName']) != "nan":
                md_content = md_content + "  - name: " + str(row['ds:DatAdditionalMaterialName']) + "\n"
                md_content = md_content + "    url: " + str(row['ds:DatAdditionalMaterialURL']) + "\n"
                md_content = md_content + "    format: " + str(row['ds:DatAdditionalMaterialFormat']) + "\n"

            md_content = md_content + "license: " + ">-\n " + str(row['license']) + "\n"

            md_content = md_content + "dataset_name: " + row['dataset_name'] + "\n"
            md_content = md_content + "location: " + row['location'] + "\n"
            md_content = md_content + "latitude_map: " + str(row['latitude_map']) + "\n"
            md_content = md_content + "longitude_map: " + str(row['longitude_map']) + "\n"
            md_content = md_content + "start_date: " + str(row['start_date']) + "\n"
            md_content = md_content + "end_date: " + str(row['end_date']) + "\n"



            md_content = md_content + "number_participants: " + str(row['number_participants']) + "\n"
            md_content = md_content + "language: " + row['language'] + "\n"
            md_content = md_content + "collection_name: " + row['collection_name'] + "\n"
            md_content = md_content + "project_url: <a href=\"" + str(row['project_url']) + "\">" + str(
                row['project_url']) + "</a>\n"

            md_content = md_content + "category: " + "\n  - " + row['category'] + "\n"
            md_content = md_content + "domain: " + "\n  - " + row['domain'] + "\n"

            md_content = md_content + "5_stars: " + str(row['5_stars']) + "\n"
            md_content = md_content + "publication_date: " + str(row['publication_date']) + "\n"
            md_content = md_content + "identifier: " + row['identifier'] + "\n"
            md_content = md_content + "request_contact: " + row['request_contact'] + "\n"

            md_content = md_content + "component_dataset_link: " + generate_html_href(row, df) + "\n"

            # Facets
            md_content = md_content + "duration_facet: " + '"' + row['duration_facet'] + '"' + "\n"
            md_content = md_content + "location_facet: " + row['location_facet'] + "\n"
            md_content = md_content + "location_continent_facet: " + row['location_continent_facet'] + "\n"

            if not str(row['data_type_facet']) == 'nan':
                md_content = md_content + "data_type_facet: " + str(row['data_type_facet']) + "\n"
            # md_content = md_content + "project_facet: " + row['project_facet'] + "\n"

            md_content = md_content + "---\n"

            output_file_path = os.path.join(output_dir, file_name)

            with open(output_file_path, 'w', encoding='utf-8') as md_file:
                md_file.write(md_content)
        except Exception as e:
            print(f"Error processing file {row['title']}: {e}")

def main(excel_path, output_dir):

    # step 1. get fields to generate project/dataset/dataset bundle
    # step 2. convertion on the existing to new
    # step 3. dynamic functions
    # step 4. facet creation

    project_fields = md.project
    dataset_fields = md.dataset

    # read by default 1st sheet of an excel file
    all_sheets = pd.read_excel(excel_path, sheet_name=None)  # None reads all sheets
    # df = pd.concat(all_sheets.values(), ignore_index=True)

    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # project
    try:
        create_project_md(all_sheets['Project'])

        create_dataset_md(all_sheets['Dataset'])

        create_bundle_md(all_sheets['Dataset Bundle'])
    except Exception as ex:
        print(ex)

    print(f"Markdown files generated in: {output_dir}")


if __name__ == "__main__":
    # Folder containing the Markdown files
    excel_path = "/Users/munkhdelger/Knowdive/LivePeople/temp/source.xlsx"

    # Output path
    output_dir = "/_datasets"
    # output_dir = "/Users/munkhdelger/Knowdive/LivePeople/temp/md"

    main(excel_path, output_dir)
