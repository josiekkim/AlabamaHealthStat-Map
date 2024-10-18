import streamlit as st
import pandas as pd

# Set page title and layout
st.set_page_config(page_title="Influenza and Pneumonia Mortality in Alabama", layout="wide")

# Influenza and Pneumonia mortality data
data_flu_pneumonia = {
    'County': ['Wilcox County', 'Lowndes County', 'Dallas County', 'Barbour County', 'Greene County',
               'Conecuh County', 'Sumter County', 'Perry County', 'Bullock County', 'Hale County'],
    'Flu and Pneumonia Death Rate (per 100,000)': [92.3, 87.6, 83.1, 79.5, 75.3, 72.8, 71.1, 69.5, 67.4, 65.9]
}

# Lowest income counties data
data_income = {
    'County': ['Perry County', 'Greene County', 'Sumter County', 'Wilcox County', 'Dallas County',
               'Barbour County', 'Conecuh County', 'Lowndes County', 'Bullock County', 'Monroe County'],
    'Per Capita Income ($)': [13833, 16425, 16977, 19031, 19653, 20074, 20756, 21298, 20783, 21885]
}

# Convert to DataFrames
df_flu_pneumonia = pd.DataFrame(data_flu_pneumonia)
df_income = pd.DataFrame(data_income)

# Display Flu and Pneumonia mortality data
st.subheader("Top 10 Counties with Highest Influenza and Pneumonia Mortality")
st.dataframe(df_flu_pneumonia)

# Display bar chart for Flu and Pneumonia mortality
st.subheader("Influenza and Pneumonia Mortality by County")
st.bar_chart(df_flu_pneumonia.set_index('County')['Flu and Pneumonia Death Rate (per 100,000)'])

# Compare with lowest income counties
st.subheader("Comparison with Lowest Income Counties")
overlap = set(df_flu_pneumonia['County']).intersection(set(df_income['County']))
st.write(f"Counties in both Flu and Pneumonia mortality and lowest income list: {', '.join(overlap) if overlap else 'No overlap.'}")

# Display lowest income counties data
st.subheader('Lowest Income Counties in Alabama')
st.dataframe(df_income)

st.write("""
Overlap with Lowest Income Counties:
The following counties overlap with the 10 lowest-income counties in Alabama:

Wilcox County
Lowndes County
Dallas County
Barbour County
Greene County
Conecuh County
Sumter County
Perry County
Bullock County
Thus, 9 out of 10 counties with the highest Influenza and Pneumonia mortality also rank among the lowest-income counties.
""")