import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title = 'EJEEP TRACKER')
st.header('The EJEEP is last seen at:')
st.header('XAVIER HALL - 12:27 PM')


excel_file = 'ejeep_logbook.xlsx'
sheet_name1 = 'LINE A'
sheet_name2 = 'LINE B'

df = pd.read_excel(excel_file,
                   engine = 'openpyxl',
                   sheet_name=sheet_name1)

df1 = pd.read_excel(excel_file,
                    engine = 'openpyxl',
                    sheet_name=sheet_name2)

st.dataframe(df)
st.dataframe(df1)