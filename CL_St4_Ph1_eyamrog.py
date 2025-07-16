# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] jp-MarkdownHeadingCollapsed=true
# 3<center>
# <img src="https://laelgelcpublic.s3.sa-east-1.amazonaws.com/lael_50_years_narrow_white.png.no_years.400px_96dpi.png" width="300" alt="LAEL 50 years logo">
# <h3>APPLIED LINGUISTICS GRADUATE PROGRAMME (LAEL)</h3>
# </center>
# <hr>

# %% [markdown]
# # Corpus Linguistics - Study 4 - Phase 1 - eyamrog

# %% [markdown]
# The aim of this phase is to consolidate `EL2AP`, `AI-EL2AP`, and `QJPP` corpora into a data set for statistical analysis.

# %% [markdown]
# ## Required Python packages

# %% [markdown]
# - pandas
# - matplotlib

# %% [markdown]
# ## Import the required libraries

# %%
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt

# %% [markdown]
# ## Define input variables

# %%
input_directory = 'cl_st4_ph1_eyamrog'
output_directory = 'cl_st4_ph1_eyamrog'

# %% [markdown]
# ## Create output directory

# %%
# Check if the output directory already exists. If it does, do nothing. If it doesn't exist, create it.
if os.path.exists(output_directory):
    print('Output directory already exists.')
else:
    try:
        os.makedirs(output_directory)
        print('Output directory successfully created.')
    except OSError as e:
        print('Failed to create the directory:', e)
        sys.exit(1)

# %% [markdown]
# ## Import the data into DataFrames

# %% [markdown]
# ### `EL2AP`

# %%
df_el2ap_dimensions = pd.read_json(f"{input_directory}/df_el2ap_dimensions.jsonl", lines=True)

# %%
df_el2ap_dimensions['Submitted'] = pd.to_datetime(df_el2ap_dimensions['Submitted'], unit='ms')
df_el2ap_dimensions['Posted'] = pd.to_datetime(df_el2ap_dimensions['Posted'], unit='ms')

# %% [markdown]
# ### `AI-EL2AP`

# %%
df_ai_el2ap_dimensions = pd.read_json(f"{input_directory}/df_ai_el2ap_dimensions.jsonl", lines=True)

# %%
df_ai_el2ap_dimensions['Submitted'] = pd.to_datetime(df_ai_el2ap_dimensions['Submitted'], unit='ms')
df_ai_el2ap_dimensions['Posted'] = pd.to_datetime(df_ai_el2ap_dimensions['Posted'], unit='ms')

# %% [markdown]
# ### `QJPP`

# %%
df_qjpp_dimensions = pd.read_json(f"{input_directory}/df_qjpp_dimensions.jsonl", lines=True)

# %%
df_qjpp_dimensions['Published'] = pd.to_datetime(df_qjpp_dimensions['Published'], unit='ms')

# %% [markdown]
# ## Reorganise `EL2AP`

# %% [markdown]
# ### Drop columns

# %%
df_el2ap_dimensions.drop(columns=['Published', 'PDF Language', 'Posted', 'Text Paragraph ChatGPT', 'AI-EL2AP Filename'], inplace=True)

# %% [markdown]
# ### Rename columns

# %%
df_el2ap_dimensions.rename(columns={'Submitted': 'Published'}, inplace=True)

# %%
df_el2ap_dimensions.rename(columns={'EL2AP Filename': 'Filename'}, inplace=True)

# %% [markdown]
# ### Create columns

# %%
df_el2ap_dimensions['Source'] = 'EL2AP'

# %%
df_el2ap_dimensions['Journal'] = 'SciELO Preprints'

# %%
df_el2ap_dimensions['Vol/Issue'] = 'Not defined'

# %%
df_el2ap_dimensions['DOI'] = 'Not defined'

# %%
df_el2ap_dimensions['ID'] = 'Not defined'

# %% [markdown]
# ### Reordering columns

# %%
ordered_columns = [
    'Source',
    'Discipline',
    'Journal',
    'Vol/Issue',
    'Published',
    'Title',
    'Authors',
    'URL',
    'DOI',
    'PDF URL',
    'ID',
    'Text ID',
    'Section',
    'Section Code',
    'Paragraph',
    'Paragraph Code',
    'Filename',
    'Text Paragraph'
]

# %%
df_el2ap_dimensions = df_el2ap_dimensions[
    ordered_columns + [col for col in df_el2ap_dimensions.columns if col not in ordered_columns]
]

# %%
df_el2ap_dimensions.columns

# %% [markdown]
# ## Reorganise `AI-EL2AP`

# %% [markdown]
# ### Drop columns

# %%
df_ai_el2ap_dimensions.drop(columns=['Published', 'PDF Language', 'Posted', 'Text Paragraph', 'EL2AP Filename'], inplace=True)

# %% [markdown]
# ### Rename columns

# %%
df_ai_el2ap_dimensions.rename(columns={'Submitted': 'Published'}, inplace=True)

# %%
df_ai_el2ap_dimensions.rename(columns={'AI-EL2AP Filename': 'Filename'}, inplace=True)

# %%
df_ai_el2ap_dimensions.rename(columns={'Text Paragraph ChatGPT': 'Text Paragraph'}, inplace=True)

# %% [markdown]
# ### Create columns

# %%
df_ai_el2ap_dimensions['Source'] = 'AI-EL2AP'

# %%
df_ai_el2ap_dimensions['Journal'] = 'SciELO Preprints'

# %%
df_ai_el2ap_dimensions['Vol/Issue'] = 'Not defined'

# %%
df_ai_el2ap_dimensions['DOI'] = 'Not defined'

# %%
df_ai_el2ap_dimensions['ID'] = 'Not defined'

# %% [markdown]
# ### Reordering columns

# %%
ordered_columns = [
    'Source',
    'Discipline',
    'Journal',
    'Vol/Issue',
    'Published',
    'Title',
    'Authors',
    'URL',
    'DOI',
    'PDF URL',
    'ID',
    'Text ID',
    'Section',
    'Section Code',
    'Paragraph',
    'Paragraph Code',
    'Filename',
    'Text Paragraph'
]

# %%
df_ai_el2ap_dimensions = df_ai_el2ap_dimensions[
    ordered_columns + [col for col in df_ai_el2ap_dimensions.columns if col not in ordered_columns]
]

# %%
df_ai_el2ap_dimensions.columns

# %% [markdown]
# ## Reorganise `QJPP`

# %% [markdown]
# ### Rename columns

# %%
df_qjpp_dimensions.rename(columns={'QJPP Filename': 'Filename'}, inplace=True)

# %% [markdown]
# ### Create columns

# %%
df_qjpp_dimensions['Source'] = 'QJPP'

# %% [markdown]
# ### Reordering columns

# %%
ordered_columns = [
    'Source',
    'Discipline',
    'Journal',
    'Vol/Issue',
    'Published',
    'Title',
    'Authors',
    'URL',
    'DOI',
    'PDF URL',
    'ID',
    'Text ID',
    'Section',
    'Section Code',
    'Paragraph',
    'Paragraph Code',
    'Filename',
    'Text Paragraph'
]

# %%
df_qjpp_dimensions = df_qjpp_dimensions[
    ordered_columns + [col for col in df_qjpp_dimensions.columns if col not in ordered_columns]
]

# %%
df_qjpp_dimensions.columns

# %% [markdown]
# ## Concatenate the DataFrames

# %%
df_cl_st1_eyamrog_dimensions = pd.concat([
    df_el2ap_dimensions,
    df_ai_el2ap_dimensions,
    df_qjpp_dimensions
], ignore_index=True)

# %% [markdown]
# ### Correcting the `Linguistic, literature and arts` discipline

# %%
df_cl_st1_eyamrog_dimensions['Discipline'] = df_cl_st1_eyamrog_dimensions['Discipline'].replace(
    'Linguistic, literature and arts', 'Linguistics, literature and arts'
)

# %% [markdown]
# ### Checking the DataFrame for missing values

# %%
df_cl_st1_eyamrog_dimensions.isna().sum()

# %%
df_cl_st1_eyamrog_dimensions.dtypes

# %%
df_cl_st1_eyamrog_dimensions

# %% [markdown]
# ## Check the presence of zero-score texts in the dimensions

# %% [markdown]
# The presence of zero-score texts seems to be insignificant.

# %%
# Counting rows where 'Factor 1 Score' is equal to zero
zero_mask = df_cl_st1_eyamrog_dimensions['Factor 1 Score'] == 0
zero_count = zero_mask.sum()
zero_indexes = df_cl_st1_eyamrog_dimensions.index[zero_mask].tolist()

print(f"Rows where 'Factor 1 Score' is zero: {zero_count}")
print(f"Indexes of those rows: {zero_indexes}")

# %%
# Counting rows where 'Factor 2 Score' is equal to zero
zero_mask = df_cl_st1_eyamrog_dimensions['Factor 2 Score'] == 0
zero_count = zero_mask.sum()
zero_indexes = df_cl_st1_eyamrog_dimensions.index[zero_mask].tolist()

print(f"Rows where 'Factor 2 Score' is zero: {zero_count}")
print(f"Indexes of those rows: {zero_indexes}")

# %%
# Counting rows where 'Factor 3 Score' is equal to zero
zero_mask = df_cl_st1_eyamrog_dimensions['Factor 3 Score'] == 0
zero_count = zero_mask.sum()
zero_indexes = df_cl_st1_eyamrog_dimensions.index[zero_mask].tolist()

print(f"Rows where 'Factor 3 Score' is zero: {zero_count}")
print(f"Indexes of those rows: {zero_indexes}")

# %%
# Counting rows where 'Factor 4 Score' is equal to zero
zero_mask = df_cl_st1_eyamrog_dimensions['Factor 4 Score'] == 0
zero_count = zero_mask.sum()
zero_indexes = df_cl_st1_eyamrog_dimensions.index[zero_mask].tolist()

print(f"Rows where 'Factor 4 Score' is zero: {zero_count}")
print(f"Indexes of those rows: {zero_indexes}")

# %%
# Counting rows where 'Factor 5 Score' is equal to zero
zero_mask = df_cl_st1_eyamrog_dimensions['Factor 5 Score'] == 0
zero_count = zero_mask.sum()
zero_indexes = df_cl_st1_eyamrog_dimensions.index[zero_mask].tolist()

print(f"Rows where 'Factor 5 Score' is zero: {zero_count}")
print(f"Indexes of those rows: {zero_indexes}")

# %% [markdown]
# ### Exporting to files

# %%
df_cl_st1_eyamrog_dimensions.to_json(f"{output_directory}/df_cl_st1_eyamrog_dimensions.jsonl", orient='records', lines=True)

# %%
df_cl_st1_eyamrog_dimensions.to_csv(f"{output_directory}/df_cl_st1_eyamrog_dimensions.tsv", sep='\t', index=False, encoding='utf-8', lineterminator='\n')

# %%
df_cl_st1_eyamrog_dimensions.to_excel(f"{output_directory}/df_cl_st1_eyamrog_dimensions.xlsx")

# %%
