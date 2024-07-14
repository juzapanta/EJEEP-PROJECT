import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title = 'EJEEP TRACKER')
st.header('The EJEEP is last seen at:')

excel_file = 'ejeep_logbook.xlsx'
sheet_name1 = 'LINE A'
sheet_name2 = 'LINE B'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name1)

df1 = pd.read_excel(excel_file,
                   sheet_name=sheet_name2)

st.dataframe(df)
st.dataframe(df1)
