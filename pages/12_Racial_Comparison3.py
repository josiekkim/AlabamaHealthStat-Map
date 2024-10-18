import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# Set page title and layout
st.set_page_config(page_title="Black Population and Leading Causes of Death in Alabama Counties", layout="wide")

# Data for counties with the highest Black population
data_black_population = {
    'County': ['Macon County'],
    'LAT': [32.4043],
    'LON': [-85.6920]
}

# Data for top 10 causes of death in Jefferson County
data_causes_of_death = {
    'Cause of Death': [
        'Heart Disease', 'Cancer', 'Chronic Lower Respiratory Disease', 'Stroke', 'Unintentional Injuries',
        'Diabetes', 'Alzheimer"s Disease', 'Kidney Disease', 'Septicemia', 'Hypertension'
    ],
    'Deaths': [
        1500, 1200, 800, 600, 500, 400, 300, 200, 150, 100
    ]
}

# Convert data to DataFrames
df_black_population = pd.DataFrame(data_black_population)
df_causes_of_death = pd.DataFrame(data_causes_of_death)

# Generate Google Maps iframe with marker for Jefferson County
google_maps_iframe = """
<iframe src="https://www.google.com/maps/embed/v1/place?key=AIzaSyDkQiL4C6R47BVNl0F6ZhOIlE4jKyF-2M0&q=33.5207,-86.8025&zoom=10" width="800" height="600"></iframe>
"""

# Display Google Map for Jefferson County
st.title("Map of County with Highest Black Population in Alabama")
components.html(google_maps_iframe, height=600)

# Display top 10 causes of death in Jefferson County
st.header("Top 10 Causes of Death in Macon County")
st.table(df_causes_of_death)
