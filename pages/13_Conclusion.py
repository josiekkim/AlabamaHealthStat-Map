import streamlit as st

# Set page title
st.title("Project Overview")

# About the project and creator
st.markdown("""
## 🎈Project Overview
This project was developed by Josie Kim, a data analyst and researcher with a passion for uncovering insights from data to improve public health outcomes. With experience in data science, I focus on combining data analysis and visualization to present meaningful stories behind the numbers.

Feel free to connect with me on:
- [Instagram](https://www.instagram.com/josiekkim/?igsh=Zm9jMWw4MGsxeWYy&utm_source=qr)  


## About the Project
This project explores the relationship between **the top 10 causes of death**, **race**, and **income** across various counties in Alabama.

### Technologies Used:
- **Python**: The core programming language used in this project.
- **Streamlit**: For creating the interactive web application.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For creating visualizations.
- **Data Sources**:  
  - U.S. Census Data for income levels.
  - CDC Mortality Data for causes of death.
  - County Health Rankings for racial demographics.

### Future Work:
- Expand the dataset to cover other states in America, creating a collective data set and a concluding map 
- Use machine learning to predict mortality rates based on socioeconomic factors.
- Cooperate with organizations to provide medical aid to areas vulnerable to diseases due to socioeconomic factors
""")

st.markdown("""
### Summary:
- Heart Disease,Cancer, Stroke, Diabetes, Kidney Disease, Liver Disease, Hypertension, and Influenza: all 9 diseases out 
of 10 diseases in total have a strong relationship of the 10 counties' mortality rates in relation to socioeconomic factors. 
Chronic Respiratory Disease didn't appear on the list assuming a good air quality for all counties in Alabama, but at least 7 
out of the 10 counties for each disease demonstrated a strong relationship between socioeconomic states of the residents and 
the mortality rate of the disease. Especially, Wilson County appears most frequently with the highest mortality rate for every 
disease in relation to socioeconomic factors, which indicates a poor medical aid given in the county. Thus, areas with lowest income, 
which are predominately constituted by African American population, account for almost all the counties that have the highest mortality rate 
for the top 10 most common diseases. The result insinuates a better medical system and information needed for particularly Wilson County and 
other 7 counties prevalent in the data. The Alabama federal government/medical organizations/institutions have to analyze and expand these data 
to maximize the provided medical aids' benefits and allocate them effectively. Extending these data and applying to the current medical system will 
significantly help the marginalized communities to acquire fair amount of medical aid to alleviate the high mortality rates. The result also highlights 
a significance in offering accessible tool for all people regardless of their socioeconomic status as previous data haphazardly woven large set of data 
that are difficult to interpret. We all need to realize a severity of the situation in discriminating people for medical aid according to their 
socioeconomic status and take an action to treat them equally.
""")































































































