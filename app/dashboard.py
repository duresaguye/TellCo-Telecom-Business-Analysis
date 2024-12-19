# dashboard.py
import streamlit as st
import pandas as pd
from src.data_extraction import df  # Assuming the df is cleaned and ready for use

# Streamlit code to display the dashboard
st.title('Telecom Data Analysis Dashboard')

# Show DataFrame preview
st.subheader('Data Preview')
st.write(df.head())

# Add other visualizations and interactivity as required (e.g., histograms, scatter plots)
