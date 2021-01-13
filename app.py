import streamlit as st
from fuzzy import get_mamdani_inference

st.sidebar.title("Prediksi Resiko Diabetes Menggunakan Fuzzy Mamdani")
st.sidebar.header("Profil Pasien: ")
age = st.sidebar.number_input("Umur")
try:
    height = st.sidebar.number_input("Tinggi Badan (cm)")
    weight = st.sidebar.number_input("Berat Badan (kg)")
    bmi = weight / ((height/100)**2)
except:
    bmi = 0

st.header("Hasil Test: ")
blood_pressure = st.number_input("Tekanan Darah")
blood_glucose = st.number_input("Gula Darah Puasa")
cholesterol = st.number_input("Kolesterol")

mamdani_value = get_mamdani_inference(age, bmi, blood_pressure, blood_glucose, cholesterol)
st.subheader("Hasil Analisis: ")
bmi_text = "Underweight" if (bmi < 18.5) else "Normal" if (bmi >= 18.5 and bmi < 25) else "Overweight" if (bmi>= 25 and bmi < 30) else "Obese"
st.write("BMI: {:.2f}".format(bmi))
st.write("Terklasifikasi : {}".format(bmi_text))
st.write("Tingkat Resiko Diabetes: {} ".format(mamdani_value))