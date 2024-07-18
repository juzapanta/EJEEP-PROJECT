import pandas as pd
import streamlit as st
import time
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

sheet_idA = '16CwByzI3-J0o36W7vs4hZ1Ovmyc2uV0DhJH4Cj96rU8'

dfA = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_idA}/export?format=csv")

st.set_page_config(
    page_title="E-jeep Tracker",
    page_icon="https://cdn-icons-png.flaticon.com/512/9249/9249336.png"
    )

line = st.selectbox(label="Choose E-jeep Line to view", options=["LINE A", "LINE B", "EXPRESS"])

st.title("Line A")
st.write(dfA.head(3))

st.title("Line B")
st.write(dfA.iloc[5:8])

st.title("Express")
st.write(dfA.iloc[10:14])

time.sleep(60 * 1) 
st.experimental_rerun()
