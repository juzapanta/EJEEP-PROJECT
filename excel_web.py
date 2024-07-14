# example/st_app.py

import pandas as pd
import streamlit as st
# import plotly.express as px

st.set_page_config(page_title = 'EJEEP TRACKER',
                   layout = 'wide')
st.header('EJEEP LAST SEEN AT:')

from datetime import datetime

# Get the current time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Display the current time in the Streamlit app
st.write("Current Time:", current_time)

line_a_df = pd.read_excel(
    io = 'ejeep_logbook.xlsx',
    engine = 'openpyxl',
    sheet_name = 'LINE A',
)

st.dataframe(line_a_df)