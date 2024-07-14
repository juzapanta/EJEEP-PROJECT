import pandas as pd
import streamlit as st
# import plotly.express as px


# CURRENT TIME
from datetime import datetime
current_date = datetime.now().strftime("%Y-%m-%d")
current_time = datetime.now().strftime("%H:%M:%S")
st.write("Today is:", current_date)
st.write("It is currently:", current_time)
st.header('EJEEP LAST SEEN AT:')

# THE THINGY
# st.set_page_config(page_title = 'EJEEP TRACKER',
#                    layout = 'wide')

# LINE A
line_a_df = pd.read_excel(
    io = 'ejeep_logbook.xlsx',
    engine = 'openpyxl',
    sheet_name = 'LINE A',
)

st.dataframe(line_a_df)