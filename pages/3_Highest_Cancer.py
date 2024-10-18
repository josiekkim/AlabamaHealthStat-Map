import streamlit as st
import pandas as pd

# Set the page title and layout
st.set_page_config(page_title="Top 10 Alabama Counties with Highest Cancer Mortality", layout="wide")

# Page title
st.title("Top 10 Counties in Alabama with Highest Cancer Mortality")

# Data for the 10 counties with the highest cancer mortality rates in Alabama
data = {
    'County': [
        'Wilcox County', 'Pickens County', 'Clarke County',
        'Henry County', 'Clay County', 'Lamar County',
        'Walker County', 'Fayette County', 'Colbert County', 'Lawrence County'
    ],
    'Cancer Death Rate (per 100,000 population)': [661.5, 662.4, 663.7, 682.1, 700.0, 701.6, 700.0, 644.9, 643.8, 639.4]
}

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Display the data in a table
st.subheader('Top 10 Counties by Cancer Mortality')
st.dataframe(df)

# Create a bar chart for cancer mortality
st.subheader('Cancer Mortality by County')
st.bar_chart(df.set_index('County')['Cancer Death Rate (per 100,000 population)'])

# Additional Information
st.write("""
This data represents the counties in Alabama with the highest mortality rates due to cancer, as recorded from 2016 to 2020. 
These regions face significant health challenges due to a combination of socioeconomic and environmental factors.
For more information, you can refer to [Stacker's report on Alabama counties with high cancer rates](https://stacker.com/alabama/counties-with-highest-cancer-rates)&#8203;:contentReference[oaicite:0]{index=0}&#8203;:contentReference[oaicite:1]{index=1}.

These counties are particularly impacted by high cancer rates due to a combination of factors such as socioeconomic disparities, limited healthcare access, and environmental conditions​(
Stacker
)​(
Alabama Public Health
).

Overlap:
Wilcox County appears in both the lowest income counties and highest cancer mortality counties.
Thus, 1 county (Wilcox County) appears in both the lists.
""")
