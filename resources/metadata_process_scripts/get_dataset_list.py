import pandas as pd
import urllib.parse



def get_link(title):
    base_url = "https://datascientiafoundation.github.io/LivePeople/datasets/"
    return base_url + urllib.parse.quote(title)

def get_parent(category, row, df_catalog):
    if category == 'Dataset Bundle':
        year_collection_city = '-'.join(row['ds:DatName'].split('-')[0:3])
        bundle_name = '-'.join(row['ds:DatName'].split('-')[3:])

        project_df = df_catalog['Project']
        project_filtered = project_df[project_df['ds:prjTitle'] == year_collection_city]

        if len(project_filtered) == 0:
            print('no project for bundle: ' + row['ds:DatName'])
            return None

        return project_filtered.iloc[0]['ds:prjIdentifier']

    elif category == 'Dataset':
        if row['ds:DatName'] == '2023-Skel-Trento-Accelerometer':
            print('')

        year_collection_city = '-'.join(row['ds:DatName'].split('-')[0:3])

        bundle_df = df_catalog['Dataset Bundle']
        bundle_filtered = bundle_df[bundle_df['ds:DatName'] == f'{year_collection_city}-{row["ds:DataTypeFacet"]}']
        if len(bundle_filtered) == 0:
            print('no bundle for ds: ' + row['ds:DatName'])
            return None

        return bundle_filtered.iloc[0]['ds:DatIdentifier']

    return None

def main(excel, output_dir):
    df_catalog = pd.read_excel(excel, sheet_name=None)
    new_df = pd.DataFrame()
    df = pd.concat([df_catalog['Dataset'], df_catalog['Dataset Bundle']], ignore_index=True)

    # dataset and bundle

    new_df['name'] = df['ds:DatName']
    new_df['identifier'] = df['ds:DatIdentifier']
    new_df['parentIdentifier'] = df.apply(lambda row: get_parent(row['ds:DatCategoryFacet'], row, df_catalog), axis=1)
    new_df['experiment'] = df['ds:DatName'].str.split('-').str[1]
    new_df['link'] = df['ds:DatName'].apply(get_link)
    new_df['sensor_name'] = df.apply(lambda row: row['ds:DatSensorName'] if row['ds:DatCategoryFacet'] == 'Dataset' else None, axis=1)
    new_df['sensor_type'] = df['ds:DatSensorType']
    new_df['isBundle'] = df['ds:DatCategoryFacet'] == 'Dataset Bundle'
    new_df['isDataset'] = df['ds:DatCategoryFacet'] == 'Dataset'
    new_df['isProject'] = False
    new_df['isVisible'] = df['ds:DatIsVisible']

    new_df['durationFacet'] = df['ds:DatDurationFacet']
    new_df['locationFacet'] = df['ds:DatLocationFacet']
    new_df['dataTypeFacet'] = df['ds:DataTypeFacet']
    new_df['categoryFacet'] = df['ds:DatCategoryFacet']
    new_df['collectionFacet'] = df['ds:DatName'].str.split('-').str[1]

    new_df['collectionFacet'] = new_df['collectionFacet'].replace({'SmartUnitn2 OSM Big Thick Data':'SmartUnitn2OSM'})

    # Add cases that have multiple parent bundles
    for id, row in new_df.iterrows():
        year_collection_city = '-'.join(row['name'].split('-')[0:3])
        bundle_name = '-'.join(row['name'].split('-')[3:])
        if 'Daily annotations & Location RD' ==  bundle_name:
            childs = new_df[new_df['name'].isin(
                [f'{year_collection_city}-Location RD', f'{year_collection_city}-Time Diaries'])]
            to_add = childs.copy()
            to_add['parentIdentifier'] = row['identifier']
            new_df = pd.concat([new_df, to_add], ignore_index=True)

    # project
    prj_df = pd.DataFrame()
    df = df_catalog['Project']

    prj_df['name'] = df['ds:prjTitle']
    prj_df['identifier'] = df['ds:prjIdentifier']
    prj_df['parentIdentifier'] = None
    prj_df['experiment'] = df['ds:prjCollectionFacet']
    prj_df['link'] = df['ds:prjTitle'].apply(get_link)
    prj_df['sensor_name'] = None
    prj_df['sensor_type'] = None

    prj_df['isBundle'] = False
    prj_df['isDataset'] = False
    prj_df['isProject'] = True
    prj_df['isVisible'] = df['ds:prjIsVisible']

    prj_df['durationFacet'] = df['ds:prjDurationFacet']
    prj_df['locationFacet'] = df['ds:prjLocationFacet']
    prj_df['dataTypeFacet'] = None
    prj_df['categoryFacet'] = df['ds:prjCategoryFacet']
    prj_df['collectionFacet'] = df['ds:prjCollectionFacet']

    out = pd.concat([new_df, prj_df], ignore_index=True)
    out = out.where(pd.notnull(out), None)
    out = out.sort_values(by='name')

    # Save the filtered DataFrame to a CSV file
    output_path = f"{output_dir}/list_of_datasets.csv"

    out.to_csv(output_path, index=False)
    print(f"Output saved to {output_path}")


    print(f"Merged : {output_dir}")


if __name__ == "__main__":
    # Folder containing the Markdown files
    excel = "/Users/munkhdelger/Knowdive/LivePeople/resources/metadata_process_scripts/sources/catalog.xlsx"

    # Output path
    output_dir = "/Users/munkhdelger/Knowdive/LivePeople/resources/metadata_process_scripts/sources"
    # output_dir = "/Users/munkhdelger/Knowdive/LivePeople/resources/metadata_process_scripts/md_new"

    main(excel, output_dir)
