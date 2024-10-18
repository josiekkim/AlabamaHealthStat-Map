import streamlit as st

# Set page title
st.title("About This Project")

# About the project and creator
st.markdown("""
## About Me
This project was developed by **[Your Name]**, a data analyst and researcher with a passion for uncovering insights from data to improve public health outcomes. With experience in data science, I focus on combining data analysis and visualization to present meaningful stories behind the numbers.

Feel free to connect with me on:
- [Instagram](https://instagram.com)  
- [Youtube](https://youtube.com)

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
- Expand the dataset to cover other states.
- Use machine learning to predict mortality rates based on socioeconomic factors.
""")
