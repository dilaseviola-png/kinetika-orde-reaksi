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

    st.subheader("Data Eksperimen")
    st.dataframe(df)

    # Ambil data
    t = df.iloc[:, 0].values
    A = df.iloc[:, 1].values

    hasil = []

    # ======================
    # ORDE 0
    # ======================
    coef0 = np.polyfit(t, A, 1)
    pred0 = np.polyval(coef0, t)
    r0 = np.corrcoef(A, pred0)[0, 1]
    r2_0 = r0**2
    k0 = abs(coef0[0])

    hasil.append(["Orde 0", r2_0, k0])

    # ======================
    # ORDE 1
    # ======================
    lnA = np.log(A)
    coef1 = np.polyfit(t, lnA, 1)
    pred1 = np.polyval(coef1, t)
    r1 = np.corrcoef(lnA, pred1)[0, 1]
    r2_1 = r1**2
    k1 = abs(coef1[0])

    hasil.append(["Orde 1", r2_1, k1])

    # ======================
    # ORDE 2
    # ======================
    invA = 1 / A
    coef2 = np.polyfit(t, invA, 1)
    pred2 = np.polyval(coef2, t)
    r2 = np.corrcoef(invA, pred2)[0, 1]
    r2_2 = r2**2
    k2 = abs(coef2[0])

    hasil.append(["Orde 2", r2_2, k2])

    # ======================
    # TABEL HASIL
    # ======================
    hasil_df = pd.DataFrame(
        hasil, columns=["Model Kinetika", "R²", "k"]
    )

    st.subheader("Hasil Analisis Kinetika")
    st.dataframe(hasil_df)

    # Tentukan orde terbaik
    orde_terbaik = hasil_df.loc[hasil_df["R²"].idxmax()]

    st.success(
        f"Reaksi paling sesuai mengikuti **{orde_terbaik['Model Kinetika']}** "
        f"dengan R² = {orde_terbaik['R²']:.3f}"
    )

    # ======================
    # INTERPRETASI
    # ======================
    st.subheader("Interpretasi")
    if orde_terbaik["Model Kinetika"] == "Orde 0":
        st.write(
            "Reaksi mengikuti kinetika orde nol, yang menunjukkan laju reaksi "
            "tidak bergantung pada konsentrasi reaktan. Model ini sering "
            "ditemukan pada proses degradasi senyawa dalam sistem pangan "
            "dengan konsentrasi reaktan tinggi."
        )
    elif orde_terbaik["Model Kinetika"] == "Orde 1":
        st.write(
            "Reaksi mengikuti kinetika orde satu, di mana laju reaksi "
            "sebanding dengan konsentrasi reaktan. Model ini umum pada "
            "reaksi degradasi senyawa bioaktif dan oksidasi."
        )
    else:
        st.write(
            "Reaksi mengikuti kinetika orde dua, yang menunjukkan laju reaksi "
            "bergantung pada interaksi dua spesies reaktan. Model ini "
            "lebih jarang ditemukan pada sistem pangan sederhana."
        )

    # ======================
    # GRAFIK
    # ======================
    st.subheader("Visualisasi Model Kinetika")

    fig, axs = plt.subplots(1, 3, figsize=(15, 4))

    axs[0].scatter(t, A)
    axs[0].plot(t, pred0)
    axs[0].set_title("Orde 0 (A vs t)")
    axs[0].set_xlabel("Waktu")
    axs[0].set_ylabel("Absorbansi")

    axs[1].scatter(t, lnA)
    axs[1].plot(t, pred1)
    axs[1].set_title("Orde 1 (ln A vs t)")
    axs[1].set_xlabel("Waktu")
    axs[1].set_ylabel("ln Absorbansi")

    axs[2].scatter(t, invA)
    axs[2].plot(t, pred2)
    axs[2].set_title("Orde 2 (1/A vs t)")
    axs[2].set_xlabel("Waktu")
    axs[2].set_ylabel("1/Absorbansi")

    st.pyplot(fig)

else:
    st.info("Silakan upload file CSV untuk memulai.")
