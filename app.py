# force redeploy

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Input")
    st.dataframe(df)

    # ======================
    # VALIDASI DATA
    # ======================
    if df.shape[1] < 2:
        st.error("❌ File CSV harus memiliki minimal 2 kolom: waktu dan absorbansi.")
        st.stop()

    # Ambil data
    t = df.iloc[:, 0].values
    A = df.iloc[:, 1].values

    if (A <= 0).any():
        st.error("❌ Nilai absorbansi harus lebih besar dari 0.")
        st.stop()

    # ======================
    # ORDE 0
    # ======================
    st.subheader("Analisis Kinetika Orde 0")

    coef = np.polyfit(t, A, 1)
    pred = np.polyval(coef, t)

    k = abs(coef[0])
    r = np.corrcoef(A, pred)[0, 1]
    r2 = r ** 2

    st.write(f"**Persamaan:** A = {coef[0]:.4f} t + {coef[1]:.4f}")
    st.write(f"**Konstanta laju (k):** {k:.5f}")
    st.write(f"**Koefisien determinasi (R²):** {r2:.3f}")

    fig, ax = plt.subplots()
    ax.scatter(t, A)
    ax.plot(t, pred)
    ax.set_xlabel("Waktu")
    ax.set_ylabel("Absorbansi")
    st.pyplot(fig)

    
