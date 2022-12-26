import process, general
import streamlit as st

st.write("# Tugas Final Project")
kalimat = st.text_input("Masukkan Kalimat Yang Ingin Diuji")
cek = st.button("Cek")

if cek:
    if general.check_alphabet(kalimat.lower().split()) == False:
        st.info("Kalimat TIDAK VALID Karena Terdapat Kata Yang Tidak Masuk Dalam Bahasa Indonesia")
    elif process.table_filling_process(kalimat.lower().split()) == True:
        st.info("Kalimat DITERIMA Karena Sesuai Dengan Pola Kalimat Bahasa Indonesia Dan Frasa Yang Disyaratkan")
    else:
        st.info("Kalimat DITOLAK Karena Tidak Sesuai Dengan Pola Kalimat Bahasa Indonesia Dan Frasa Yang Disyaratkan")
