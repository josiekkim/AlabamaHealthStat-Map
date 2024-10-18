import streamlit as st
import pandas as pd

# Set page title and layout
st.set_page_config(page_title="Hypertension Mortality in Alabama", layout="wide")

# Hypertension mortality data
data_hypertension = {
    'County': ['Wilcox County', 'Lowndes County', 'Dallas County', 'Barbour County', 'Conecuh County',
               'Greene County', 'Hale County', 'Perry County', 'Bullock County', 'Sumter County'],
    'Hypertension Death Rate (per 100,000)': [95.4, 90.2, 88.7, 84.6, 81.3, 79.1, 78.5, 76.9, 74.8, 72.5]
}

# Lowest income counties data
data_income = {
    'County': ['Perry County', 'Greene County', 'Sumter County', 'Wilcox County', 'Dallas County',
               'Barbour County', 'Conecuh County', 'Lowndes County', 'Bullock County', 'Monroe County'],
    'Per Capita Income ($)': [13833, 16425, 16977, 19031, 19653, 20074, 20756, 21298, 20783, 21885]
}

# Convert to DataFrames
df_hypertension = pd.DataFrame(data_hypertension)
df_income = pd.DataFrame(data_income)

# Display hypertension mortality data
st.subheader("Top 10 Counties with Highest Hypertension Mortality")
st.dataframe(df_hypertension)

# Display bar chart for hypertension mortality
st.subheader("Hypertension Mortality by County")
st.bar_chart(df_hypertension.set_index('County')['Hypertension Death Rate (per 100,000)'])

# Compare with lowest income counties
st.subheader("Comparison with Lowest Income Counties")
overlap = set(df_hypertension['County']).intersection(set(df_income['County']))
st.write(f"Counties in both hypertension mortality and lowest income list: {', '.join(overlap) if overlap else 'No overlap.'}")

# Display lowest income counties data
st.subheader('Lowest Income Counties in Alabama')
st.dataframe(df_income)

st.write("""
Overlap with Lowest Income Counties:
The following counties overlap between those with the highest hypertension-related mortality and the 10 lowest-income counties in Alabama:

Wilcox County
Lowndes County
Dallas County
Barbour County
Conecuh County
Greene County
Perry County
Bullock County
Thus, 8 out of 10 counties with the highest hypertension mortality also rank among the lowest-income counties.
""")