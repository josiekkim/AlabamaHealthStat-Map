import streamlit as st
import pandas as pd

# Set page title and layout
st.set_page_config(page_title="Chronic Liver Disease Mortality in Alabama", layout="wide")

# Liver disease mortality data
data_liver = {
    'County': ['Wilcox County', 'Lowndes County', 'Dallas County', 'Barbour County', 'Conecuh County',
               'Perry County', 'Bullock County', 'Hale County', 'Greene County', 'Sumter County'],
    'Liver Disease Death Rate (per 100,000)': [75.3, 72.8, 70.2, 68.4, 66.9, 64.5, 63.2, 62.1, 61.8, 60.4]
}

# Lowest income counties data
data_income = {
    'County': ['Perry County', 'Greene County', 'Sumter County', 'Wilcox County', 'Dallas County',
               'Barbour County', 'Conecuh County', 'Lowndes County', 'Bullock County', 'Monroe County'],
    'Per Capita Income ($)': [13833, 16425, 16977, 19031, 19653, 20074, 20756, 21298, 20783, 21885]
}

# Convert to DataFrames
df_liver = pd.DataFrame(data_liver)
df_income = pd.DataFrame(data_income)

# Display liver disease mortality data
st.subheader("Top 10 Counties with Highest Liver Disease Mortality")
st.dataframe(df_liver)

# Display bar chart for liver disease mortality
st.subheader("Liver Disease Mortality by County")
st.bar_chart(df_liver.set_index('County')['Liver Disease Death Rate (per 100,000)'])

# Compare with lowest income counties
st.subheader("Comparison with Lowest Income Counties")
overlap = set(df_liver['County']).intersection(set(df_income['County']))
st.write(f"Counties in both liver disease mortality and lowest income list: {', '.join(overlap) if overlap else 'No overlap.'}")

# Display lowest income counties data
st.subheader('Lowest Income Counties in Alabama')
st.dataframe(df_income)

st.write("""
Overlap with Lowest Income Counties:
There is significant overlap between counties with high chronic liver disease mortality and those with the lowest income. The following counties appear in both lists:

Wilcox County
Lowndes County
Dallas County
Barbour County
Conecuh County
Perry County
Bullock County
Greene County
Thus, 8 out of 10 counties with high liver disease mortality also rank among the lowest-income counties.
""")
