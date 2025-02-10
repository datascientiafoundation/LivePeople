import pandas as pd
import re
import os

# Load the Excel file
excel_file = "/resources/metadata_process_scripts/sources/2024-LivePeople_Metadata_Description-v2.xlsx"

# Read both sheets
projects_df = pd.read_excel(excel_file, sheet_name="LivePeople PROJECTS Metadata", usecols=["Field", "Description", "Visibility"])
datasets_df = pd.read_excel(excel_file, sheet_name="LivePeople DATASETS Metadata", usecols=["Field", "Description", "Visibility"])

# Merge both dataframes
combined_df = pd.concat([projects_df, datasets_df]).drop_duplicates().reset_index(drop=True)
combined_df = combined_df.dropna(subset=["Field"])
combined_df['Description'] = combined_df['Description'].fillna('')

combined_df = combined_df[combined_df["Field"].str.startswith("ds:")]
combined_df = combined_df[~combined_df['Field'].str.contains('ds:prjDocumentationURL', case=False, na=False)]
combined_df = combined_df[~combined_df['Field'].str.contains('ds:prjDocumentationFormat', case=False, na=False)]
combined_df = combined_df[~combined_df['Field'].str.contains('ds:prjAdditionalMaterialURL', case=False, na=False)]
combined_df = combined_df[~combined_df['Field'].str.contains('ds:prjAdditionalMaterialFormat', case=False, na=False)]
combined_df = combined_df[~combined_df['Field'].str.contains('ds:DatDownloadRequestURL', case=False, na=False)]
combined_df = combined_df[~combined_df['Field'].str.contains('ds:DatDownloadRequestFormat', case=False, na=False)]
combined_df = combined_df[~combined_df['Field'].str.contains('ds:DatDocumentationURL', case=False, na=False)]
combined_df = combined_df[~combined_df['Field'].str.contains('ds:DatDocumentationFormat', case=False, na=False)]
combined_df = combined_df[~combined_df['Field'].str.contains('ds:DatAdditionalMaterialURL', case=False, na=False)]
combined_df = combined_df[~combined_df['Field'].str.contains('ds:DatAdditionalMaterialFormat', case=False, na=False)]
combined_df = combined_df[~combined_df['Field'].str.contains('ds:DatCodebookURL', case=False, na=False)]
combined_df = combined_df[~combined_df['Field'].str.contains('ds:DatCodebookFormat', case=False, na=False)]


# Function to convert to human-readable format
def convert_to_human_readable(field):
    # Remove 'ds:' prefix
    field = re.sub(r'^ds:', '', field)

    # Replace uppercase letters followed by lowercase with a space and lowercase letter
    field = re.sub(r'([a-z])([A-Z])', r'\1 \2', field)

    # only first letter upper
    field = field[0].capitalize() + field[1:].lower()

    # Replace 'Prj' with 'Project' and 'Dat' with 'Data'
    field = field.replace('Prj', 'Project').replace('Dat', 'Data')
    field = field.replace('irbapproval', 'IRB approval')
    field = field.replace('datae', 'date')
    field = field.replace('Datais', 'Data is')


    return field


def escape_pipe_in_description(description):
    return description.replace('|', r'\|')

# Filter data based on visibility
combined_df = combined_df[combined_df['Visibility'] == 'public']
combined_df['Field HR'] = combined_df['Field'].apply(convert_to_human_readable)
combined_df['Field HR'] = combined_df['Field HR'].replace({'': ''})

combined_df['Description'] = combined_df['Description'].apply(escape_pipe_in_description)




# Generate Markdown content
markdown_content = """---
title: metadata
layout: base
permalink: /metadata/
---

| Field Name       | Description                                        |
|------------------|----------------------------------------------------|
"""

# Append field names and descriptions
for _, row in combined_df.iterrows():
    field_hr = row['Field HR']
    # Replace spaces with non-breaking spaces for field names
    field_hr = field_hr.replace(' ', '&nbsp;')

    description = row['Description']
    markdown_content += f"| **{field_hr}** | {description} |\n"

# Define the output path (root directory)
output_dir = "/"  # Root folder path
output_file = os.path.join(output_dir, "metadata.md")

# Save to the Markdown file in the root folder
with open(output_file, "w", encoding="utf-8") as md_file:
    md_file.write(markdown_content)

print(f"Markdown file 'metadata.md' has been generated successfully in {output_dir}.")
