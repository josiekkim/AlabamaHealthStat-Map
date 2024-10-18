import streamlit as st
import pandas as pd

# Set page title and layout
st.set_page_config(page_title="Alzheimer's Mortality in Alabama", layout="wide")

# Alzheimer's data
data_alzheimer = {
    'County': ['Shelby County', 'Mobile County', 'Jefferson County', 'Montgomery County', 'Tuscaloosa County',
               'Baldwin County', 'Madison County', 'Limestone County', 'Elmore County', 'Etowah County'],
    'Alzheimer Death Rate (per 100,000)': [70, 68, 67, 65, 64, 63, 62, 61, 60, 59]
}

# Lowest income data
data_income = {
    'County': ['Perry County', 'Greene County', 'Sumter County', 'Wilcox County', 'Dallas County',
               'Barbour County', 'Conecuh County', 'Lowndes County', 'Bullock County', 'Monroe County'],
    'Per Capita Income ($)': [13833, 16425, 16977, 19031, 19653, 20074, 20756, 21298, 20783, 21885]
}

# Convert to DataFrames
df_alzheimer = pd.DataFrame(data_alzheimer)
df_income = pd.DataFrame(data_income)

# Display Alzheimer's mortality data
st.subheader("Top 10 Counties with Highest Alzheimer's Mortality")
st.dataframe(df_alzheimer)

# Display bar chart for Alzheimer's mortality
st.subheader("Alzheimer's Mortality by County")
st.bar_chart(df_alzheimer.set_index('County')['Alzheimer Death Rate (per 100,000)'])

# Compare with lowest income counties
st.subheader("Comparison with Lowest Income Counties")
overlap = set(df_alzheimer['County']).intersection(set(df_income['County']))
st.write(f"Counties in both Alzheimer's mortality and lowest income list: {', '.join(overlap) if overlap else 'No overlap.'}")

# Display lowest income data
st.subheader('Lowest Income Counties in Alabama')
st.dataframe(df_income)

st.write(""" 
Comparison with the Lowest Income Counties:
When we compare the counties with the highest Alzheimer's mortality to the 10 lowest-income counties in Alabama, none of the counties overlap. This indicates that, while Alzheimer's affects all parts of the state, the counties with the highest rates are generally not the same as those with the lowest income levels.
""")