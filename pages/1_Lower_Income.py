import streamlit as st
import pandas as pd

# Set the page title and layout
st.set_page_config(page_title="Lowest Income Counties in Alabama", layout="wide")

# Page title
st.title("Top 10 Counties in Alabama with the Lowest Per Capita Income")

# Data for the 10 lowest-income counties in Alabama (from Wikipedia)
data = {
    'County': [
        'Perry County', 'Greene County', 'Sumter County', 'Wilcox County', 'Dallas County',
        'Barbour County', 'Conecuh County', 'Lowndes County', 'Bullock County', 'Monroe County'
    ],
    'Per Capita Income ($)': [13833, 16425, 16977, 19031, 19653, 20074, 20756, 21298, 20783, 21885]
}

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Sort the DataFrame by Per Capita Income
df_sorted = df.sort_values(by='Per Capita Income ($)', ascending=True)

# Display the data in a table
st.subheader('Income Distribution in the 10 Poorest Counties in Alabama')
st.dataframe(df_sorted)

# Create a bar chart for per capita income in ascending order
st.subheader('Per Capita Income by County (Sorted)')
st.bar_chart(df_sorted.set_index('County')['Per Capita Income ($)'])

# Additional Information
st.write("""
This data represents the counties in Alabama with the lowest per capita income based on the 2020 census. These regions face economic challenges and have higher poverty rates, requiring targeted support.
""")
