
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Kinetika Orde Reaksi",
    layout="wide"
)

menu = st.sidebar.radio(
    "Navigasi",
    ["🏠 Dashboard", "📈 Analisis Kinetika", "📄 Tentang"]
)

if menu == "🏠 Dashboard":
    st.title("📊 Dashboard Kinetika Reaksi")

    st.markdown("""
    ### 👋 Selamat datang!
    Aplikasi ini digunakan untuk **menentukan orde reaksi kimia**
    berdasarkan data **waktu–absorbansi** dari hasil eksperimen.

    #### 🔬 Apa yang bisa dilakukan aplikasi ini?
    - Menentukan orde reaksi **0, 1, dan 2**
    - Menghitung **konstanta laju reaksi (k)**
    - Menampilkan **grafik linearitas**
    - Menentukan orde reaksi **paling sesuai berdasarkan R²**

    #### 🧪 Contoh penerapan:
    - Kinetika degradasi zat pangan
    - Reaksi enzimatik
    - Studi kestabilan nanomaterial
    """)

    st.info("📌 Pilih menu **Analisis Kinetika** di sidebar untuk mulai.")

elif menu == "📈 Analisis Kinetika":
    st.title("📈 Analisis Kinetika Orde Reaksi")

    uploaded_file = st.file_uploader(
        "Upload file CSV (waktu, absorbansi)",
        type=["csv"]
    )

    # ... (kode analisis kamu yang sudah jadi)

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

elif menu == "📄 Tentang":
    st.title("📄 Tentang Aplikasi")

    st.markdown("""
    **Aplikasi Kinetika Orde Reaksi**

    Dibuat menggunakan:
    - Python
    - Streamlit
    - Pandas & NumPy

    Tujuan aplikasi ini adalah membantu analisis kinetika reaksi
    secara **interaktif dan visual**, khususnya pada bidang
    **kimia terapan dan pangan**.
    """)
