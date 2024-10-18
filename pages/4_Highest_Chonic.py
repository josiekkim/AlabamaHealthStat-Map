import streamlit as st
import pandas as pd

# Set the page title and layout
st.set_page_config(page_title="Top 10 Alabama Counties with Highest Chronic Lower Respiratory Disease Mortality", layout="wide")

# Page title
st.title("Top 10 Counties in Alabama with Highest Chronic Lower Respiratory Disease Mortality")

# Data for the 10 counties with highest chronic lower respiratory disease mortality in Alabama
data = {
    'County': [
        'Tallapoosa County', 'Covington County', 'Butler County',
        'Chilton County', 'Walker County', 'Fayette County',
        'DeKalb County', 'Cullman County', 'Geneva County', 'Lawrence County'
    ],
    'Mortality Rate (per 100,000 population)': [125, 122, 118, 115, 110, 109, 107, 106, 104, 103]
}

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Display the data in a table
st.subheader('Top 10 Counties by Chronic Lower Respiratory Disease Mortality')
st.dataframe(df)

# Create a bar chart for chronic lower respiratory disease mortality
st.subheader('Chronic Lower Respiratory Disease Mortality by County')
st.bar_chart(df.set_index('County')['Mortality Rate (per 100,000 population)'])

# Additional Information
st.write("""
This data represents the counties in Alabama with the highest mortality rates due to chronic lower respiratory diseases.
These regions often experience higher rates due to factors such as smoking, air quality, and access to healthcare services.
For more information, you can refer to the Alabama Department of Public Health's [County Health Profiles](https://www.alabamapublichealth.gov/healthstats/assets/chp2020.pdf).

Overlap:
None of the counties from the lowest income list overlap with the counties experiencing the highest Chronic Lower Respiratory Disease mortality.
""")
