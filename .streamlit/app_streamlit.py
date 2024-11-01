import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1dEkzg2yVLVDFRnjKJf7LsFTkzsse1mDPEHkol9J1kg4/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, usecols=[0, 1])
st.dataframe(data)
