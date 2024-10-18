import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import matplotlib.pyplot as plt

# Set page title and layout
st.set_page_config(page_title="Macon and Winston Counties: Demographics and Leading Causes of Death", layout="wide")

# Data for racial demographics in Macon and Winston Counties
data_racial_demographics = {
    'County': ['Macon County', 'Winston County'],
    'Black or African American (%)': [82.6, 1.2],
    'White (%)': [15.2, 96.3],
    'Hispanic or Latino (%)': [1.0, 1.5],
    'Asian (%)': [0.5, 0.3],
    'Other (%)': [0.7, 0.7]
}

# Data for top 3 causes of death in Macon and Winston Counties
data_causes_of_death = {
    'County': ['Macon County', 'Macon County', 'Macon County', 'Winston County', 'Winston County', 'Winston County'],
    'Cause of Death': [
        'Heart Disease', 'Cancer', 'Chronic Lower Respiratory Disease',
        'Heart Disease', 'Cancer', 'Chronic Lower Respiratory Disease'
    ],
    'Deaths': [150, 120, 80, 180, 160, 90]
}

# Convert data to DataFrames
df_racial_demographics = pd.DataFrame(data_racial_demographics)
df_causes_of_death = pd.DataFrame(data_causes_of_death)

# Display racial demographics
st.title("Racial Demographics in Macon and Winston Counties")
st.table(df_racial_demographics)

# Display top 3 causes of death
st.header("Top 3 Causes of Death in Macon and Winston Counties")
st.table(df_causes_of_death)

# Plotting bar chart for top 3 causes of death
st.header("Bar Chart of Top 3 Causes of Death in Macon and Winston Counties")
fig, ax = plt.subplots()
df_causes_of_death.pivot(index='Cause of Death', columns='County', values='Deaths').plot(kind='bar', ax=ax, color=['#FFA500', '#8FDFF5'])
plt.title("Top 3 Causes of Death by County")
plt.xlabel("Cause of Death")
plt.ylabel("Number of Deaths")
plt.xticks(rotation=45)
st.pyplot(fig)
