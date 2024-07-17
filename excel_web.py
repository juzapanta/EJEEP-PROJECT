import pandas as pd
import streamlit as st
import time

sheet_id = '16CwByzI3-J0o36W7vs4hZ1Ovmyc2uV0DhJH4Cj96rU8'

df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

st.write(df)

time.sleep(60 * 1)  # Refresh every 5 minutes (adjust as needed)
st.experimental_rerun()
