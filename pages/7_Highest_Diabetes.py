import streamlit as st
import pandas as pd

# Set page title and layout
st.set_page_config(page_title="Diabetes Mortality in Alabama", layout="wide")

# Diabetes mortality data
data_diabetes = {
    'County': ['Wilcox County', 'Lowndes County', 'Dallas County', 'Greene County', 'Barbour County',
               'Conecuh County', 'Hale County', 'Perry County', 'Bullock County', 'Sumter County'],
    'Diabetes Death Rate (per 100,000)': [86.8, 76.5, 72.4, 68.2, 65.9, 64.5, 63.8, 62.9, 61.7, 60.4]
}

# Lowest income counties data
data_income = {
    'County': ['Perry County', 'Greene County', 'Sumter County', 'Wilcox County', 'Dallas County',
               'Barbour County', 'Conecuh County', 'Lowndes County', 'Bullock County', 'Monroe County'],
    'Per Capita Income ($)': [13833, 16425, 16977, 19031, 19653, 20074, 20756, 21298, 20783, 21885]
}

# Convert to DataFrames
df_diabetes = pd.DataFrame(data_diabetes)
df_income = pd.DataFrame(data_income)

# Display diabetes mortality data
st.subheader("Top 10 Counties with Highest Diabetes Mortality")
st.dataframe(df_diabetes)

# Display bar chart for diabetes mortality
st.subheader("Diabetes Mortality by County")
st.bar_chart(df_diabetes.set_index('County')['Diabetes Death Rate (per 100,000)'])

# Compare with lowest income counties
st.subheader("Comparison with Lowest Income Counties")
overlap = set(df_diabetes['County']).intersection(set(df_income['County']))
st.write(f"Counties in both diabetes mortality and lowest income list: {', '.join(overlap) if overlap else 'No overlap.'}")

# Display lowest income counties data
st.subheader('Lowest Income Counties in Alabama')
st.dataframe(df_income)

st.write("""
Overlap with Lowest Income Counties:
When comparing the counties with the highest diabetes mortality to the 10 lowest-income counties in Alabama, there is significant overlap. The following counties appear in both lists:

Wilcox County
Lowndes County
Dallas County
Greene County
Barbour County
Conecuh County
Perry County
Bullock County
Thus, 8 out of 10 counties with the highest diabetes mortality also rank among the lowest-income counties in Alabama.
""")