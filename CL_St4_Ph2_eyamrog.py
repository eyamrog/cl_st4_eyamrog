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
# <center>
# <img src="https://laelgelcpublic.s3.sa-east-1.amazonaws.com/lael_50_years_narrow_white.png.no_years.400px_96dpi.png" width="300" alt="LAEL 50 years logo">
# <h3>APPLIED LINGUISTICS GRADUATE PROGRAMME (LAEL)</h3>
# </center>
# <hr>

# %% [markdown]
# # Corpus Linguistics - Study 4 - Phase 2 - eyamrog

# %% [markdown]
# The aim of this phase is to calculate the `QJPP`, `EL2AP`, and `EL2AP` registers mean dimension scores.

# %% [markdown]
# ## Definitions

# %% [markdown]
# ### Corpora

# %% [markdown]
# - `QJPP` - Quality Journals Published Papers: Published Papers Reference Corpus
# - `EL2AP` - English-as-L2 Authored Papers: Human-Authored Target Corpus extracted from the SciELO Preprints archive
# - `AI-EL2AP` - AI English-as-L2 Authored Papers: AI-Generated Target Corpus

# %% [markdown]
# ### Multi-Dimensional Analysis of English (Biber, 1988) five major dimensions of variation

# %% [markdown]
# - `Dimension 1` - Involved versus Informational Production
# - `Dimension 2` - Narrative Concerns
# - `Dimension 3` - Explicit versus Situation-Dependent Reference
# - `Dimension 4` - Overt Expression of Argumentation
# - `Dimension 5` - Abstract versus Non-Abstract Style

# %% [markdown]
# ## Required Python packages

# %% [markdown]
# - pandas
# - matplotlib
# - seaborn

# %% [markdown]
# ## Import the required libraries

# %%
import pandas as pd
import os
import sys
import seaborn as sns
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
# ## Calculate the mean dimension score

# %%
def mean_dimension_score(dimension, source, discipline='All'):
    if discipline == 'All':
        mean_score = df_cl_st1_eyamrog_dimensions.loc[
            df_cl_st1_eyamrog_dimensions['Source'] == source,
            dimension
        ].mean()
    else:
        mean_score = df_cl_st1_eyamrog_dimensions.loc[
            (df_cl_st1_eyamrog_dimensions['Source'] == source) &
            (df_cl_st1_eyamrog_dimensions['Discipline'] == discipline),
            dimension
        ].mean()
    return mean_score


# %% [markdown]
# ## Boxplot by Source

# %%
def boxplot_by_source(plot_filepath, dimension, discipline='All'):
    # Custom category orders
    custom_order = ['QJPP', 'EL2AP', 'AI-EL2AP']
    if discipline == 'All':
        subset = df_cl_st1_eyamrog_dimensions.copy()
        title = f"{dimension} by Source - All Disciplines"
    else:
        subset = df_cl_st1_eyamrog_dimensions[
            df_cl_st1_eyamrog_dimensions['Discipline'] == discipline
        ]
        title = f"{dimension} by Source - {discipline}"
    
    # Create the boxplot
    plt.figure(figsize=(10, 6))
    sns.boxplot(
        data=subset,
        x='Source',
        y=dimension,
        color='royalblue',
        order=custom_order,
        showfliers=False
    )
    plt.title(title)
    plt.xlabel("Source")
    plt.ylabel(dimension)
    plt.grid(True)
    plt.tight_layout()

    # Saving as an image
    plt.savefig(plot_filepath, dpi=300, bbox_inches='tight')

    plt.show()


# %%
def boxplot_by_source_by_discipline(plot_filepath, dimension):
    # Custom category orders
    custom_order1 = ['QJPP', 'EL2AP', 'AI-EL2AP']
    custom_order2 = [
        'Health Sciences',
        'Biological Sciences',
        'Human Sciences',
        'Applied Social Sciences',
        'Linguistics, literature and arts'
    ]
    # Make a safe copy of the DataFrame
    df = df_cl_st1_eyamrog_dimensions.copy()

    # Apply the custom categorical ordering
    df['Source'] = pd.Categorical(df['Source'], categories=custom_order1, ordered=True)
    df['Discipline'] = pd.Categorical(df['Discipline'], categories=custom_order2, ordered=True)

    # Boxplot by Source and Discipline
    plt.figure(figsize=(14, 6))
    sns.boxplot(
        data=df,
        x='Discipline',
        y=dimension,
        hue='Source',
        showfliers=False
    )
    plt.title(f"{dimension} by Source and Discipline")
    plt.xlabel('Source')
    plt.ylabel(dimension)
    plt.legend(title='Discipline', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    plt.tight_layout()

    # Saving as an image
    plt.savefig(plot_filepath, dpi=300, bbox_inches='tight')

    plt.show()


# %% [markdown]
# ## Import the data into a DataFrame

# %% [markdown]
# ### `CL_St1_eyamrog`

# %%
df_cl_st1_eyamrog_dimensions = pd.read_json(f"{input_directory}/df_cl_st1_eyamrog_dimensions.jsonl", lines=True)

# %%
df_cl_st1_eyamrog_dimensions['Published'] = pd.to_datetime(df_cl_st1_eyamrog_dimensions['Published'], unit='ms')

# %% [markdown]
# ## Inspecting the most informational AI-revised texts with the respective original texts

# %%
# Filter for Source == 'AI-EL2AP'
df_filtered = df_cl_st1_eyamrog_dimensions[df_cl_st1_eyamrog_dimensions['Source'] == 'AI-EL2AP']

# Sort by Dimension 1 ascending and get the bottom 5
lowest_scores = df_filtered.nsmallest(10, 'Dimension 1')

# Return the indexes
top_ai_informational_indexes = lowest_scores.index.tolist()
top_ai_informational_indexes

# %%
# Step 2: Extract and normalise the filenames
top_informational_filenames = (
    df_cl_st1_eyamrog_dimensions.loc[top_ai_informational_indexes, 'Filename']
    .str.replace('ai-', '', regex=False)
)

# Step 3: Filter rows from EL2AP that match the cleaned filenames
matching_rows = df_cl_st1_eyamrog_dimensions[
    (df_cl_st1_eyamrog_dimensions['Source'] == 'EL2AP') &
    (df_cl_st1_eyamrog_dimensions['Filename'].isin(top_informational_filenames))
]

# Step 4: Get their indexes
top_informational_indexes = matching_rows.index.tolist()
print(matching_indexes)

# %%
# Step 1: Extract and convert filenames from the AI-EL2AP entries
top_ai_informational_filenames = df_cl_st1_eyamrog_dimensions.loc[top_ai_informational_indexes, 'Filename']
top_informational_filenames = top_ai_informational_filenames.str.replace('ai-', '', regex=False)

# Step 2: Match them to EL2AP entries in the same order
top_informational_indexes = [
    df_cl_st1_eyamrog_dimensions[
        (df_cl_st1_eyamrog_dimensions['Source'] == 'EL2AP') &
        (df_cl_st1_eyamrog_dimensions['Filename'] == fname)
    ].index[0]  # Assumes one match per filename
    for fname in top_informational_filenames
]

top_informational_indexes

# %%
# Create the two individual DataFrames first
df_ai = df_cl_st1_eyamrog_dimensions.loc[top_ai_informational_indexes, ['Dimension 1', 'Text Paragraph']]
df_el2 = df_cl_st1_eyamrog_dimensions.loc[top_informational_indexes, ['Dimension 1', 'Text Paragraph']]

# Rename columns for clarity
df_ai = df_ai.rename(columns={
    'Dimension 1': 'AI-EL2AP Score',
    'Text Paragraph': 'AI-EL2AP Text Paragraph'
})

df_el2 = df_el2.rename(columns={
    'Dimension 1': 'EL2AP Score',
    'Text Paragraph': 'EL2AP Text Paragraph'
})

# Combine them side-by-side using the matching index order
df_top_informational = pd.concat([df_ai.reset_index(drop=True), df_el2[['EL2AP Score', 'EL2AP Text Paragraph']].reset_index(drop=True)], axis=1)

# Optional: preview the result
df_top_informational

# %%
df_top_informational.loc[4, 'EL2AP Text Paragraph']

# %%
df_top_informational.loc[4, 'AI-EL2AP Text Paragraph']

# %%
df_top_informational.loc[2, 'EL2AP Text Paragraph']

# %%
df_top_informational.loc[2, 'AI-EL2AP Text Paragraph']

# %%
df_top_informational.loc[6, 'EL2AP Text Paragraph']

# %%
df_top_informational.loc[6, 'AI-EL2AP Text Paragraph']

# %% [markdown]
# ## Mean Dimension Scores - Source by Discipline per Dimension

# %% [markdown]
# ### Create the required lists

# %% [markdown]
# #### dimensions

# %%
dimensions = [col for col in df_cl_st1_eyamrog_dimensions.columns if 'Factor' in col]
dimensions

# %%
dimension_labels = [
    'Dimension 1',
    'Dimension 2',
    'Dimension 3',
    'Dimension 4',
    'Dimension 5'
]

# %%
# Create a mapping from old names to new names
rename_map = dict(zip(dimensions, dimension_labels))

# Rename the columns in the DataFrame
df_cl_st1_eyamrog_dimensions = df_cl_st1_eyamrog_dimensions.rename(columns=rename_map)

# %%
dimensions = [col for col in df_cl_st1_eyamrog_dimensions.columns if 'Dimension' in col]
dimensions

# %% [markdown]
# #### sources

# %%
custom_order = [
    'QJPP',
    'EL2AP',
    'AI-EL2AP'
]
sources = [src for src in custom_order if src in df_cl_st1_eyamrog_dimensions['Source'].unique()]
sources

# %% [markdown]
# #### disciplines

# %%
custom_order = [
    'Health Sciences',
    'Biological Sciences',
    'Human Sciences',
    'Applied Social Sciences',
    'Linguistics, literature and arts'
]
disciplines = [src for src in custom_order if src in df_cl_st1_eyamrog_dimensions['Discipline'].unique()]
disciplines = ['All'] + disciplines
disciplines

# %% [markdown]
# ### Mean Dimension Scores

# %%
# Build the nested dictionary
mean_dimension_score_dict = {
    dim: {
        f"{disc} {src}": mean_dimension_score(dim, src, disc)
        for disc in disciplines
        for src in sources
    }
    for dim in dimensions
}

# %%
df_mean_dimension_score = pd.DataFrame(mean_dimension_score_dict)
df_mean_dimension_score.index.name = 'Source by Discipline'

# %%
df_mean_dimension_score

# %% [markdown]
# #### Create a LaTeX table

# %%
title = 'Mean Dimension Scores - Source by Discipline per Dimension'
filename = 'df_mean_dimension_score'

# %%
caption = title
label = f"tab:{filename}"
tex_filename = f"{filename}.tex"

# %%
tex_table = df_mean_dimension_score.to_latex(float_format='%.2f', longtable=True, decimal='.', caption=caption, label=label)

# %%
with open(f"{output_directory}/{tex_filename}", 'w', encoding='utf8', newline='\n') as file:
    file.write(tex_table)

# %% [markdown]
# ## Boxplots

# %% [markdown]
# ### `Dimension 1`

# %% [markdown]
# #### `All` disciplines

# %%
filename = 'dim1_by_source_all_disciplines'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 1', 'All')

# %% [markdown]
# #### `Health Sciences` discipline

# %%
filename = 'dim1_by_source_health_sciences'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 1', 'Health Sciences')

# %% [markdown]
# #### `Biological Sciences` discipline

# %%
filename = 'dim1_by_source_biological_sciences'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 1', 'Biological Sciences')

# %% [markdown]
# #### `Human Sciences` discipline

# %%
filename = 'dim1_by_source_human_sciences'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 1', 'Human Sciences')

# %% [markdown]
# #### `Applied Social Sciences` discipline

# %%
filename = 'dim1_by_source_applied_social_sciences'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 1', 'Applied Social Sciences')

# %% [markdown]
# #### `Linguistics, literature and arts` discipline

# %%
filename = 'dim1_by_source_linguistics_literature_arts'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 1', 'Linguistics, literature and arts')

# %% [markdown]
# #### By source by discipline

# %%
filename = 'dim1_by_source_by_discipline'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source_by_discipline(plot_filepath, 'Dimension 1')

# %% [markdown]
# ### `Dimension 2`

# %% [markdown]
# #### `All` disciplines

# %%
filename = 'dim2_by_source_all_disciplines'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 2', 'All')

# %% [markdown]
# #### `Health Sciences` discipline

# %%
filename = 'dim2_by_source_health_sciences'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 2', 'Health Sciences')

# %% [markdown]
# #### `Biological Sciences` discipline

# %%
filename = 'dim2_by_source_biological_sciences'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 2', 'Biological Sciences')

# %% [markdown]
# #### `Human Sciences` discipline

# %%
filename = 'dim2_by_source_human_sciences'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 2', 'Human Sciences')

# %% [markdown]
# #### `Applied Social Sciences` discipline

# %%
filename = 'dim2_by_source_applied_social_sciences'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 2', 'Applied Social Sciences')

# %% [markdown]
# #### `Linguistics, literature and arts` discipline

# %%
filename = 'dim2_by_source_linguistics_literature_arts'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 2', 'Linguistics, literature and arts')

# %% [markdown]
# #### By source by discipline

# %%
filename = 'dim2_by_source_by_discipline'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source_by_discipline(plot_filepath, 'Dimension 2')

# %% [markdown]
# ### `Dimension 3`

# %% [markdown]
# #### `All` disciplines

# %%
filename = 'dim3_by_source_all_disciplines'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 3', 'All')

# %% [markdown]
# #### `Health Sciences` discipline

# %%
filename = 'dim3_by_source_health_sciences'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 3', 'Health Sciences')

# %% [markdown]
# #### `Biological Sciences` discipline

# %%
filename = 'dim3_by_source_biological_sciences'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 3', 'Biological Sciences')

# %% [markdown]
# #### `Human Sciences` discipline

# %%
filename = 'dim3_by_source_human_sciences'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 3', 'Human Sciences')

# %% [markdown]
# #### `Applied Social Sciences` discipline

# %%
filename = 'dim3_by_source_applied_social_sciences'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 3', 'Applied Social Sciences')

# %% [markdown]
# #### `Linguistics, literature and arts` discipline

# %%
filename = 'dim3_by_source_linguistics_literature_arts'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 3', 'Linguistics, literature and arts')

# %% [markdown]
# #### By source by discipline

# %%
filename = 'dim3_by_source_by_discipline'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source_by_discipline(plot_filepath, 'Dimension 3')

# %% [markdown]
# ### `Dimension 4`

# %% [markdown]
# #### `All` disciplines

# %%
filename = 'dim4_by_source_all_disciplines'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 4', 'All')

# %% [markdown]
# #### `Health Sciences` discipline

# %%
filename = 'dim4_by_source_health_sciences'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 4', 'Health Sciences')

# %% [markdown]
# #### `Biological Sciences` discipline

# %%
filename = 'dim4_by_source_biological_sciences'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 4', 'Biological Sciences')

# %% [markdown]
# #### `Human Sciences` discipline

# %%
filename = 'dim4_by_source_human_sciences'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 4', 'Human Sciences')

# %% [markdown]
# #### `Applied Social Sciences` discipline

# %%
filename = 'dim4_by_source_applied_social_sciences'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 4', 'Applied Social Sciences')

# %% [markdown]
# #### `Linguistics, literature and arts` discipline

# %%
filename = 'dim4_by_source_linguistics_literature_arts'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 4', 'Linguistics, literature and arts')

# %% [markdown]
# #### By source by discipline

# %%
filename = 'dim4_by_source_by_discipline'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source_by_discipline(plot_filepath, 'Dimension 4')

# %% [markdown]
# ### `Dimension 5`

# %% [markdown]
# #### `All` disciplines

# %%
filename = 'dim5_by_source_all_disciplines'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 5', 'All')

# %% [markdown]
# #### `Health Sciences` discipline

# %%
filename = 'dim5_by_source_health_sciences'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 5', 'Health Sciences')

# %% [markdown]
# #### `Biological Sciences` discipline

# %%
filename = 'dim5_by_source_biological_sciences'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 5', 'Biological Sciences')

# %% [markdown]
# #### `Human Sciences` discipline

# %%
filename = 'dim5_by_source_human_sciences'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 5', 'Human Sciences')

# %% [markdown]
# #### `Applied Social Sciences` discipline

# %%
filename = 'dim5_by_source_applied_social_sciences'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 5', 'Applied Social Sciences')

# %% [markdown]
# #### `Linguistics, literature and arts` discipline

# %%
filename = 'dim5_by_source_linguistics_literature_arts'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source(plot_filepath, 'Dimension 5', 'Linguistics, literature and arts')

# %% [markdown]
# #### By source by discipline

# %%
filename = 'dim5_by_source_by_discipline'
plot_filepath = f"{output_directory}/{filename}.png"
boxplot_by_source_by_discipline(plot_filepath, 'Dimension 5')

# %% [markdown]
# ## Prepare data set for SAS

# %% [markdown]
# There may be issues when importing data into SAS. In order to minimise them:
#
# - Limit the columns to the ones really needed
# - Avoid using headers with long labels and spaces

# %%
df_cl_st1_eyamrog_dimensions.columns

# %%
unused_columns = [
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
    'Text Paragraph',
    'Type/Token',
    'Word Length',
    'Word Count'
]
df_cl_st1_eyamrog_dimensions_sas = df_cl_st1_eyamrog_dimensions.drop(columns=unused_columns)

# %% [markdown]
# ### Exporting to files

# %%
df_cl_st1_eyamrog_dimensions_sas.to_json(f"{output_directory}/df_cl_st1_eyamrog_dimensions_sas.jsonl", orient='records', lines=True)

# %%
df_cl_st1_eyamrog_dimensions_sas.to_csv(f"{output_directory}/df_cl_st1_eyamrog_dimensions_sas.tsv", sep='\t', index=False, encoding='utf-8', lineterminator='\n')

# %%
df_cl_st1_eyamrog_dimensions_sas.to_excel(f"{output_directory}/df_cl_st1_eyamrog_dimensions_sas.xlsx")

# %%
