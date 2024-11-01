import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuración de las credenciales
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/AYACDA23/Desktop/COTIZADOR/creacion-de-proformas-5e0ad4fa1176.json", scope)  # Coloca la ruta a tu archivo JSON
client = gspread.authorize(creds)

# Abre la hoja de cálculo
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1dEkzg2yVLVDFRnjKJf7LsFTkzsse1mDPEHkol9J1kg4/edit?gid=528600400#gid=528600400")
worksheet = sheet.get_worksheet(2)  # Selecciona la primera hoja

# Obtén los datos y muéstralos en Streamlit
data = worksheet.get_all_records()
st.dataframe(data)
