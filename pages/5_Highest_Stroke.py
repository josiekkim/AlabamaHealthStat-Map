import streamlit as st
import pandas as pd

# Set the page title and layout
st.set_page_config(page_title="Top 10 Alabama Counties with Highest Stroke Mortality", layout="wide")

# Page title
st.title("Top 10 Counties in Alabama with Highest Stroke Mortality")

# Data for top 10 counties with stroke mortality
data_stroke = {
    'County': ['Shelby County', 'Dallas County', 'Wilcox County', 'Lowndes County', 'Barbour County',
               'Conecuh County', 'Greene County', 'Bullock County', 'Hale County', 'Perry County'],
    'Stroke Death Rate (per 100,000 population)': [142.1, 120.5, 118.3, 115.7, 110.1, 108.5, 106.4, 104.9, 103.2, 100.7]
}

# Data for lowest income counties
data_income = {
    'County': ['Perry County', 'Greene County', 'Sumter County', 'Wilcox County', 'Dallas County',
               'Barbour County', 'Conecuh County', 'Lowndes County', 'Bullock County', 'Monroe County'],
    'Per Capita Income ($)': [13833, 16425, 16977, 19031, 19653, 20074, 20756, 21298, 20783, 21885]
}

# Convert data to DataFrames
df_stroke = pd.DataFrame(data_stroke)
df_income = pd.DataFrame(data_income)

# Display stroke mortality data
st.subheader('Top 10 Counties by Stroke Mortality')
st.dataframe(df_stroke)

# Display bar chart for stroke mortality
st.subheader('Stroke Mortality by County')
st.bar_chart(df_stroke.set_index('County')['Stroke Death Rate (per 100,000 population)'])

# Check for overlap with lowest-income counties
st.subheader('Comparison with Lowest Income Counties')
overlap = set(df_stroke['County']).intersection(set(df_income['County']))
st.write(f"Counties in both stroke mortality and lowest income list: {', '.join(overlap)}")

# Display the income data
st.subheader('Lowest Income Counties')
st.dataframe(df_income)

# Additional Information
st.write("""
This data represents counties in Alabama with the highest stroke mortality and compares them to the counties with the lowest income. 
Seven counties overlap between these lists, indicating a potential link between socioeconomic conditions and stroke mortality.

Overlap with the Lowest Income Counties:
The following counties overlap with the 10 lowest income counties:

Wilcox County
Lowndes County
Barbour County
Conecuh County
Greene County
Bullock County
Perry County
Thus, 7 counties overlap between stroke mortality and low income counties.
""")
