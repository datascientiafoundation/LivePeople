import pandas as pd
import urllib.parse



def get_link(title):
    base_url = "https://datascientiafoundation.github.io/LivePeople/datasets/"
    return base_url + urllib.parse.quote(title)

def main(excel, output_dir):
    df_catalog = pd.read_excel(excel, sheet_name=None)

    df = pd.concat([df_catalog['Dataset'], df_catalog['Dataset Bundle']], ignore_index=True)

    df['experiment'] = df['ds:DatName'].str.split('-').str[1]
    df['isBundle'] = df['ds:DatCategoryFacet'] == 'Dataset Bundle'
    df['link'] = df['ds:DatName'].apply(get_link)
    df['ds:prjCollectionFacet'] =df['experiment']

    columns = ['ds:DatName', 'ds:DatIdentifier', 'experiment', 'ds:DatSensorName', 'ds:DatSensorType', 'isBundle', 'link']
    facet_columns = [col for col in df.columns if 'Facet' in col]

    # Combine explicit columns and facet columns
    columns = columns + facet_columns

    out = df[columns]
    # Save the filtered DataFrame to a CSV file
    output_path = f"{output_dir}/list_of_datasets.csv"

    out.to_csv(output_path, index=False)
    print(f"Output saved to {output_path}")


    print(f"Merged : {output_dir}")


if __name__ == "__main__":
    # Folder containing the Markdown files
    excel = "//Users/munkhdelger/Knowdive/LivePeople/resources/metadata_process_scripts/source.xlsx"

    # Output path
    output_dir = "/Users/munkhdelger/Knowdive/LivePeople/resources/metadata_process_scripts/sources"
    # output_dir = "/Users/munkhdelger/Knowdive/LivePeople/resources/metadata_process_scripts/md_new"

    main(excel, output_dir)
