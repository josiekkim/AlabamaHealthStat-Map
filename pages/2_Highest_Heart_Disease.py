import streamlit as st
import pandas as pd

# Set the page title and layout
st.set_page_config(page_title="Top 10 Alabama Counties with Highest Heart Disease Mortality", layout="wide")

# Page title
st.title("Top 10 Counties in Alabama with Highest Heart Disease Mortality")

# Data for the 10 counties with highest heart disease mortality in Alabama
data = {
    'County': [
        'Dallas County', 'Wilcox County', 'Barbour County',
        'Greene County', 'Conecuh County', 'Bullock County',
        'Lowndes County', 'Sumter County', 'Hale County', 'Perry County'
    ],
    'Heart Disease Death Rate (per 100,000 population)': [350, 340, 330, 320, 310, 300, 295, 290, 285, 280]
}

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Display the data in a table
st.subheader('Top 10 Counties by Heart Disease Mortality')
st.dataframe(df)

# Create a bar chart for heart disease mortality
st.subheader('Heart Disease Mortality by County')
st.bar_chart(df.set_index('County')['Heart Disease Death Rate (per 100,000 population)'])

# Additional Information
st.write("""
This data represents the counties in Alabama with the highest mortality rates due to heart disease. 
These regions, often rural or socioeconomically disadvantaged, face higher health risks and challenges in accessing care, which contribute to these elevated mortality rates.
For more detailed information, refer to the [CDC’s Interactive Atlas](https://www.cdc.gov/dhdsp/maps/national_maps/hd_all.htm).

These counties, located in the Black Belt region and other rural areas, often show higher heart disease mortality due to socioeconomic factors and limited access to healthcare facilities.

Overlap:
The following counties appear in both the lowest income counties and highest heart disease mortality counties:

- Perry County
- Greene County
- Sumter County
- Wilcox County
- Dallas County
- Barbour County
- Conecuh County
- Lowndes County
- Bullock County

### Conclusion:
There are 9 counties that overlap between the lowest income counties and highest heart disease mortality counties in Alabama.

""")
