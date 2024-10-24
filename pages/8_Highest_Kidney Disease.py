import streamlit as st
import pandas as pd

# Set page title and layout
st.set_page_config(page_title="Kidney Disease Mortality in Alabama", layout="wide")

# Kidney disease mortality data
data_kidney = {
    'County': ['Wilcox County', 'Lowndes County', 'Dallas County', 'Greene County', 'Conecuh County',
               'Barbour County', 'Bullock County', 'Perry County', 'Hale County', 'Sumter County'],
    'Kidney Disease Death Rate (per 100,000)': [85.3, 78.6, 76.2, 73.9, 72.1, 70.3, 69.8, 68.7, 66.5, 64.2]
}

# Lowest income counties data
data_income = {
    'County': ['Perry County', 'Greene County', 'Sumter County', 'Wilcox County', 'Dallas County',
               'Barbour County', 'Conecuh County', 'Lowndes County', 'Bullock County', 'Monroe County'],
    'Per Capita Income ($)': [13833, 16425, 16977, 19031, 19653, 20074, 20756, 21298, 20783, 21885]
}

# Convert to DataFrames
df_kidney = pd.DataFrame(data_kidney)
df_income = pd.DataFrame(data_income)

# Display kidney disease mortality data
st.subheader("Top 10 Counties with Highest Kidney Disease Mortality")
st.dataframe(df_kidney)

# Display bar chart for kidney disease mortality
st.subheader("Kidney Disease Mortality by County")
st.bar_chart(df_kidney.set_index('County')['Kidney Disease Death Rate (per 100,000)'])

# Compare with lowest income counties
st.subheader("Comparison with Lowest Income Counties")
overlap = set(df_kidney['County']).intersection(set(df_income['County']))
st.write(f"Counties in both kidney disease mortality and lowest income list: {', '.join(overlap) if overlap else 'No overlap.'}")

# Display lowest income counties data
st.subheader('Lowest Income Counties in Alabama')
st.dataframe(df_income)

st.write("""
Overlap with Lowest Income Counties:
Wilcox County
Lowndes County
Dallas County
Greene County
Conecuh County
Barbour County
Bullock County
Perry County
8 out of 10 counties overlap with the lowest-income counties.
""")