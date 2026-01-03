import streamlit as st
import pandas as pd

st.set_page_config(page_title="Kinetika Orde Reaksi")

st.title("Penentuan Orde Reaksi")
st.write("Upload data waktu dan absorbansi (CSV)")

uploaded_file = st.file_uploader(
    "Upload file CSV (kolom 1 = waktu, kolom 2 = absorbansi)",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Input")
    st.dataframe(df)
else:
    st.info("Silakan upload file CSV untuk memulai.")
