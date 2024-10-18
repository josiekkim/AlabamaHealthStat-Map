import streamlit as st
import pandas as pd

# Set the page title and layout
st.set_page_config(page_title="Leading Causes of Death in Alabama", layout="wide")

# Page title
st.title('Alabama’s Leading Causes of Death (Top 10)')

# Mock data for Alabama's leading causes of death (you can replace this with actual data)
data = {
    'Cause of Death': [
        'Heart Disease', 'Cancer', 'Chronic Lower Respiratory Diseases',
        'Stroke', 'Alzheimer\'s Disease', 'Diabetes',
        'Kidney Disease', 'Influenza and Pneumonia', 'Chronic Liver Disease', 'Hypertension'
    ],
    'Deaths (per 100,000 population)': [200, 180, 150, 120, 100, 90, 80, 70, 60, 50]
}

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Display the data in a table
st.subheader('Top 10 Causes of Death in Alabama')
st.dataframe(df)

# Create a bar chart
st.subheader('Deaths by Cause (per 100,000 population)')
st.bar_chart(df.set_index('Cause of Death'))

# Additional Information
st.write("""
This data represents the top 10 leading causes of death in Alabama. 
The death rate is expressed as the number of deaths per 100,000 population. 
Heart disease and cancer continue to be the primary causes of mortality in the state.
""")
