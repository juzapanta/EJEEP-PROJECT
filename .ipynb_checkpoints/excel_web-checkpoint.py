import pandas as pd
import streamlit as st
# import plotly.express as px
from datetime import datetime


# CURRENT TIME
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
current_time = now.strftime("%H:%M:%S")
st.write("Today is:", current_date)
st.write("Current Time:", current_time)

# LINE A
line_a_df = pd.read_excel(
    io = 'ejeep_logbook.xlsx',
    engine = 'openpyxl',
    sheet_name = 'LINE A',
)


# LINE B
line_b_df = pd.read_excel(
    io = 'ejeep_logbook.xlsx',
    engine = 'openpyxl',
    sheet_name = 'LINE B',
)

st.dataframe(line_a_df)
st.dataframe(line_b_df)