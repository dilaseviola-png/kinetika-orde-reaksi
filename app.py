import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ======================
# KONFIGURASI HALAMAN
# ======================
st.set_page_config(
    page_title="Kinetika Orde Reaksi",
    layout="wide"
)

# ======================
# SIDEBAR NAVIGASI
# ======================
menu = st.sidebar.radio(
    "Navigasi",
    ["🏠 Dashboard", "📈 Analisis Kinetika", "📄 Tentang"]
)

# ======================
# HALAMAN DASHBOARD
# ======================
if menu == "🏠 Dashboard":
    st.title("📊 Dashboard Kinetika Orde Reaksi")

    st.markdown("""
    ### 👋 Selamat datang!
    Aplikasi ini digunakan untuk **menentukan orde reaksi kimia**
    berdasarkan data **waktu–absorbansi** hasil eksperimen.

    #### 🔬 Fitur utama:
    - Analisis kinetika **orde 0, 1, dan 2**
    - Perhitungan **konstanta laju reaksi (k)**
    - Visualisasi grafik linearitas
    - Penentuan orde reaksi terbaik berdasarkan **R²**

    #### 🍽️🧪 Bidang penerapan:
    - Kimia pangan (degradasi, stabilitas)
    - Reaksi enzimatik
    - Nanoteknologi dan material
    """)

    st.info("➡️ Pilih menu **Analisis Kinetika** di sidebar untuk memulai.")

# ======================
# HALAMAN ANALISIS
# ======================
elif menu == "📈 Analisis Kinetika":
    st.title("📈 Analisis Kinetika Orde Reaksi")

    uploaded_file = st.file_uploader(
        "Upload file CSV (kolom: waktu, absorbansi)",
        type=["csv"]
    )

    if uploaded_file is None:
        st.info("Silakan upload file CSV untuk memulai analisis.")
        st.stop()

    # ======================
    # BACA CSV (AUTO DELIMITER)
    # ======================
    df = pd.read_csv(uploaded_file, sep=None, engine="python")

    st.subheader("📄 Data Eksperimen")
    st.dataframe(df)

    st.write("Jumlah kolom:", df.shape[1])

    # ======================
    # VALIDASI DATA
    # ======================
    if df.shape[1] < 2:
        st.error("❌ File CSV harus memiliki minimal 2 kolom (waktu dan absorbansi).")
        st.stop()

    col_waktu = df.columns[0]
    col_abs = df.columns[1]

    t = df[col_waktu].values
    A = df[col_abs].values

    if (A <= 0).any():
        st.error("❌ Nilai absorbansi harus lebih besar dari 0.")
        st.stop()

    st.success("✅ Data valid, analisis dilakukan.")

    # ======================
    # ORDE 0
    # ======================
    st.subheader("🔹 Analisis Orde 0")

    coef0 = np.polyfit(t, A, 1)
    pred0 = np.polyval(coef0, t)
    k0 = abs(coef0[0])
    r2_0 = np.corrcoef(A, pred0)[0, 1] ** 2

    st.write(f"Persamaan: A = {coef0[0]:.4f} t + {coef0[1]:.4f}")
    st.write(f"k = {k0:.5f}")
    st.write(f"R² = {r2_0:.4f}")

    fig0, ax0 = plt.subplots()
    ax0.scatter(t, A, label="Data")
    ax0.plot(t, pred0, label="Regresi")
    ax0.set_xlabel("Waktu")
    ax0.set_ylabel("Absorbansi")
    ax0.set_title("Orde 0: Absorbansi vs Waktu")
    ax0.legend()
    st.pyplot(fig0)

    # ======================
    # ORDE 1
    # ======================
    st.subheader("🔹 Analisis Orde 1")

    lnA = np.log(A)
    coef1 = np.polyfit(t, lnA, 1)
    pred1 = np.polyval(coef1, t)
    k1 = abs(coef1[0])
    r2_1 = np.corrcoef(lnA, pred1)[0, 1] ** 2

    st.write(f"Persamaan: ln A = {coef1[0]:.4f} t + {coef1[1]:.4f}")
    st.write(f"k = {k1:.5f}")
    st.write(f"R² = {r2_1:.4f}")

    fig1, ax1 = plt.subplots()
    ax1.scatter(t, lnA, label="Data")
    ax1.plot(t, pred1, label="Regresi")
    ax1.set_xlabel("Waktu")
    ax1.set_ylabel("ln Absorbansi")
    ax1.set_title("Orde 1: ln Absorbansi vs Waktu")
    ax1.legend()
    st.pyplot(fig1)

    # ======================
    # ORDE 2
    # ======================
    st.subheader("🔹 Analisis Orde 2")

    invA = 1 / A
    coef2 = np.polyfit(t, invA, 1)
    pred2 = np.polyval(coef2, t)
    k2 = abs(coef2[0])
    r2_2 = np.corrcoef(invA, pred2)[0, 1] ** 2

    st.write(f"Persamaan: 1/A = {coef2[0]:.4f} t + {coef2[1]:.4f}")
    st.write(f"k = {k2:.5f}")
    st.write(f"R² = {r2_2:.4f}")

    fig2, ax2 = plt.subplots()
    ax2.scatter(t, invA, label="Data")
    ax2.plot(t, pred2, label="Regresi")
    ax2.set_xlabel("Waktu")
    ax2.set_ylabel("1/Absorbansi")
    ax2.set_title("Orde 2: 1/Absorbansi vs Waktu")
    ax2.legend()
    st.pyplot(fig2)

    # ======================
    # KESIMPULAN
    # ======================
    st.subheader("📌 Kesimpulan Orde Reaksi")

    hasil = {
        "Orde 0": r2_0,
        "Orde 1": r2_1,
        "Orde 2": r2_2
    }

    orde_terbaik = max(hasil, key=hasil.get)

    st.metric("Orde Reaksi Terbaik", orde_terbaik)
    st.write("Nilai R² tertinggi menunjukkan orde reaksi yang paling sesuai.")

# ======================
# HALAMAN TENTANG APLIKASI
# ======================
elif menu == "📄 Tentang":
    st.title("📄 Tentang Aplikasi")

    st.markdown("""
    **Aplikasi Kinetika Orde Reaksi**  
    Dibuat untuk membantu analisis data kinetika reaksi secara
    **interaktif dan visual**.

    **Metode analisis:**
    - Orde 0: Absorbansi vs Waktu
    - Orde 1: ln Absorbansi vs Waktu
    - Orde 2: 1/Absorbansi vs Waktu

    **Teknologi yang digunakan:**
    - Python
    - Streamlit
    - Pandas, NumPy, Matplotlib

    **Bidang aplikasi:**
    Kimia terapan, pangan, dan nanoteknologi.
    """)

    st.subheader("👥 Profil Anggota Kelompok 7")

    anggota = [
        {"nama": "Dila Seviola", "nim": "2450152"},
        {"nama": "Hegar Sutania", "nim": "2450164"},
        {"nama": "Maher Abdul Jabbar", "nim": "2450176"},
        {"nama": "Naufal Maulana Bakhtiyar", "nim": "2450192"},
        {"nama": "Zahraeka Ambiya", "nim": "2450207"},
    ]

    for a in anggota:
        st.markdown(f"""
        **{a['nama']}**  
        NIM: {a['nim']}  
        DIV – Nanoteknologi Pangan  
        """)
        st.markdown("---")
