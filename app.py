# force redeploy

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sidebar Navigation
page = st.sidebar.selectbox(
    "📄 Go to Page",
    ("Dashboard", "Upload Data", "Finance Chatbot", "Settings")
)

st.set_page_config(page_title="Penentuan Orde Reaksi", layout="centered")

st.title("Penentuan Orde Reaksi")
st.write(
    "Aplikasi ini menentukan orde reaksi berdasarkan data waktu dan absorbansi "
    "menggunakan pendekatan kinetika orde 0, 1, dan 2."
)

uploaded_file = st.file_uploader(
    "Upload file CSV (kolom 1 = waktu, kolom 2 = absorbansi)",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep=None, engine="python")

    st.subheader("Data Input")
    st.dataframe(df)

    st.write("Kolom terdeteksi:", df.columns)
    st.write("Jumlah kolom:", df.shape[1])

    if df.shape[1] < 2:
        st.error("❌ File CSV tidak terbaca sebagai 2 kolom. Cek delimiter CSV.")
        st.stop()

    t = df.iloc[:, 0].values
    A = df.iloc[:, 1].values

    if (A <= 0).any():
        st.error("❌ Nilai absorbansi harus > 0")
        st.stop()

    st.success("✅ Data valid, analisis bisa dilakukan")

