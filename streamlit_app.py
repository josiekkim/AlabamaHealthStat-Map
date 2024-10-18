# streamlit run Home.py
import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Alabama's Top 10 Causes of Death: Race and Income Analysis", layout="wide")

# Markdown introduction
st.markdown("""
# ss Alabama's Top 10 Causes of Death: Analyzing the Relationship with Race and Income

## Project Overview

This project seeks to uncover the relationships between **Alabama's top 10 causes of death**, **racial demographics**, and **income distribution** across different counties. By examining these factors, we aim to identify potential disparities in health outcomes across various socioeconomic and racial groups in Alabama.

### Key Objectives:
- **Identify the top 10 causes of death** in Alabama by county.
- **Analyze racial demographics** in counties with the highest mortality rates for each cause of death.
- **Investigate the income distribution** in counties with high mortality rates and compare income levels to racial data.

## Causes of Death

The leading causes of death in Alabama, based on recent data, include:
1. **Heart Disease**
2. **Cancer**
3. **Chronic Lower Respiratory Diseases**
4. **Stroke**
5. **Alzheimer's Disease**
6. **Diabetes**
7. **Kidney Disease**
8. **Influenza and Pneumonia**
9. **Chronic Liver Disease**
10. **Hypertension**

## Methodology

We will analyze data from the following sources:
- **U.S. Census Data**: To retrieve income distribution by county.
- **CDC Mortality Data**: For the top causes of death across Alabama counties.
- **County Health Rankings**: For racial and income distribution data.

### Steps:
1. Identify the top 10 causes of death across Alabama counties.
2. Collect racial demographics for each county.
3. Gather per capita income data for each county.
4. Cross-analyze the mortality rates with income and racial data to identify correlations.

## Expected Outcomes

Through this analysis, we expect to find:
- Counties with lower income levels may experience higher mortality rates for certain causes of death.
- There may be significant racial disparities in health outcomes, with certain racial groups being more vulnerable to specific diseases.
- Income may play a major role in access to healthcare and preventive measures, leading to higher death rates in lower-income counties.

---

## Visualizing the Data

Below, we will display charts showing the correlations between the top causes of death, income, and racial demographics in Alabama.
""")

# Add placeholders for charts that you can later integrate with your data
st.write("### Mortality by County and Cause of Death")
# Placeholder for actual chart
st.write("*(Chart to be added here)*")

st.write("### Racial Demographics and Income Correlation")
# Placeholder for another chart
st.write("*(Chart to be added here)*")


# https://www.alabamapublichealth.gov/healthstats/