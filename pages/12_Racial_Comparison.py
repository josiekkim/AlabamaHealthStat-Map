import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page title and layout
st.set_page_config(page_title="Racial Demographics of Alabama Counties by Income", layout="wide")

# Data for racial demographics in highest-income counties
data_race_high_income = {
    'County': ['Shelby County', 'Madison County', 'Limestone County', 'Baldwin County', 'Tuscaloosa County',
               'Jefferson County', 'Montgomery County', 'Elmore County', 'Lee County', 'Mobile County'],
    'Per Capita Income ($)': [66345, 61252, 53944, 56747, 49199, 47586, 41232, 53944, 45046, 46691],
    'White (%)': [79, 68, 77, 82, 58, 52, 32, 70, 72, 58],
    'African American (%)': [14, 25, 18, 13, 37, 44, 62, 25, 22, 37],
    'Other (%)': [7, 7, 5, 5, 5, 4, 6, 5, 6, 5]
}

# Data for racial demographics in lowest-income counties
data_race_low_income = {
    'County': ['Perry County', 'Greene County', 'Sumter County', 'Wilcox County', 'Dallas County',
               'Barbour County', 'Conecuh County', 'Lowndes County', 'Bullock County', 'Monroe County'],
    'Per Capita Income ($)': [13833, 16425, 16977, 19031, 19653, 20074, 20756, 21298, 20783, 21885],
    'White (%)': [30, 18, 23, 26, 30, 53, 47, 25, 28, 59],
    'African American (%)': [68, 81, 75, 72, 69, 45, 50, 74, 70, 39],
    'Other (%)': [2, 1, 2, 2, 1, 2, 3, 1, 2, 2]
}

# Convert the data into pandas DataFrames
df_race_high_income = pd.DataFrame(data_race_high_income)
df_race_low_income = pd.DataFrame(data_race_low_income)

# Sort both DataFrames by income in ascending order
df_race_high_income_sorted = df_race_high_income.sort_values(by='Per Capita Income ($)', ascending=True)
df_race_low_income_sorted = df_race_low_income.sort_values(by='Per Capita Income ($)', ascending=True)

# Create two columns for side-by-side charts
col1, col2 = st.columns(2)

# Display high-income county racial demographics in the first column
with col1:
    st.subheader("Highest Income Counties (Sorted by Income)")
    st.dataframe(df_race_high_income_sorted)

    # Create a stacked bar chart for racial demographics of high-income counties, sorted by income
    fig, ax = plt.subplots(figsize=(8, 6))
    df_race_high_income_sorted.set_index('County')[['White (%)', 'African American (%)', 'Other (%)']].plot(
        kind='bar', stacked=True, ax=ax, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
    plt.title("Racial Demographics in Highest Income Counties")
    plt.ylabel("Percentage")
    plt.xlabel("County (Sorted by Income)")
    plt.legend(title="Racial Group")
    st.pyplot(fig)

# Display low-income county racial demographics in the second column
with col2:
    st.subheader("Lowest Income Counties (Sorted by Income)")
    st.dataframe(df_race_low_income_sorted)

    # Create a stacked bar chart for racial demographics of low-income counties, sorted by income
    fig, ax = plt.subplots(figsize=(8, 6))
    df_race_low_income_sorted.set_index('County')[['White (%)', 'African American (%)', 'Other (%)']].plot(
        kind='bar', stacked=True, ax=ax, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
    plt.title("Racial Demographics in Lowest Income Counties")
    plt.ylabel("Percentage")
    plt.xlabel("County (Sorted by Income)")
    plt.legend(title="Racial Group")
    st.pyplot(fig)
