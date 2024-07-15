import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection
import plotly.express as px
from datetime import datetime


# CURRENT TIME
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
current_time = now.strftime("%H:%M:%S")
st.write("Today is:", current_date)
st.write("Current Time:", current_time)

st.header('EJEEPS LAST SEEN AT')

conn = st.experimental_connection("gsheets", type = GSheetsConnection)

existing_data = conn.read(worksheet = "Sheet1", usecols=list(range(6)), ttl=5)
existing_data = existing_data.dropna(how = "all")

st.dataframe(existing_data)

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

# EXPRESS
line_express_df = pd.read_excel(
    io = 'ejeep_logbook.xlsx',
    engine = 'openpyxl',
    sheet_name = 'EXPRESS',
)

st.dataframe(line_a_df)
st.dataframe(line_b_df)
st.dataframe(line_express_df)
