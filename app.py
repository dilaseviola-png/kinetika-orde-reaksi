import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

    # Ambil data
    t = df.iloc[:, 0].values
    A = df.iloc[:, 1].values

    # ======================
    # ORDE 0
    # ======================
    st.subheader("Analisis Kinetika Orde 0")

    # Regresi linier A vs t
    coef = np.polyfit(t, A, 1)
    pred = np.polyval(coef, t)

    k = abs(coef[0])
    r = np.corrcoef(A, pred)[0, 1]
    r2 = r ** 2

    # Tampilkan hasil numerik
    st.write(f"**Persamaan:** A = {coef[0]:.4f} t + {coef[1]:.4f}")
    st.write(f"**Konstanta laju (k):** {k:.5f}")
    st.write(f"**Koefisien korelasi (r):** {r:.3f}")
    st.write(f"**Koefisien determinasi (R²):** {r2:.3f}")

    # Interpretasi singkat
    st.write(
        "📌 *Jika hubungan absorbansi terhadap waktu linear dengan nilai R² tinggi, "
        "maka reaksi dapat mengikuti kinetika orde nol.*"
    )

    # Grafik
    fig, ax = plt.subplots()
    ax.scatter(t, A, label="Data eksperimen")
    ax.plot(t, pred, label="Regresi linier")
    ax.set_xlabel("Waktu")
    ax.set_ylabel("Absorbansi")
    ax.set_title("Orde 0: Absorbansi vs Waktu")
    ax.legend()

    st.pyplot(fig)

else:
    st.info("Silakan upload file CSV untuk memulai.")
