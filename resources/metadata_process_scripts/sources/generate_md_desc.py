import pandas as pd
import re
import os

# Load the Excel file
excel_file = "/Users/munkhdelger/Knowdive/LivePeople/resources/metadata_process_scripts/sources/2024-LivePeople_Metadata_Description-v2.xlsx"

# Read both sheets
projects_df = pd.read_excel(excel_file, sheet_name="LivePeople PROJECTS Metadata", usecols=["Field", "Description", "Visibility"])
datasets_df = pd.read_excel(excel_file, sheet_name="LivePeople DATASETS Metadata", usecols=["Field", "Description", "Visibility"])

# Merge both dataframes
combined_df = pd.concat([projects_df, datasets_df]).drop_duplicates().reset_index(drop=True)
combined_df = combined_df.dropna(subset=["Field"])
combined_df = combined_df[combined_df["Field"].str.startswith("ds:")]

# Function to convert to human-readable format
def convert_to_human_readable(field):
    # Remove 'ds:' prefix
    field = re.sub(r'^ds:', '', field)

    # Replace 'Prj' with 'Project' and 'Dat' with 'Data'
    field = field.replace('prj', 'Project').replace('Dat', 'Data')

    # Replace uppercase letters followed by lowercase with a space and lowercase letter
    field = re.sub(r'([a-z])([A-Z])', r'\1 \2', field)

    # only first letter upper
    field = field[0].capitalize() + field[1:].lower()

    # Correct common typos or inconsistencies, e.g., 'Datae' -> 'Date'
    field = field.replace('Datae', 'Date')

    return field

# Filter data based on visibility
combined_df = combined_df[combined_df['Visibility'] == 'public']
combined_df['Field HR'] = combined_df['Field'].apply(convert_to_human_readable)

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
    markdown_content += f"| **{row['Field HR']}** | {row['Description']} |\n"

# Define the output path (root directory)
output_dir = "/Users/munkhdelger/Knowdive/LivePeople"  # Root folder path
output_file = os.path.join(output_dir, "metadata.md")

# Save to the Markdown file in the root folder
with open(output_file, "w", encoding="utf-8") as md_file:
    md_file.write(markdown_content)

print(f"Markdown file 'metadata.md' has been generated successfully in {output_dir}.")
