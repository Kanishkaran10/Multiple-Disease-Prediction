import streamlit as st
import pickle as pkl
import numpy as np
import pandas as pd
st.set_page_config(page_title="Multiple Disease Prediction", layout="centered")
st.title("Multi Disease Prediction System")

disease = st.sidebar.selectbox("Select a Disease to predict",["Parkinson's Disease", "Kidney Disease", "Liver Disease"])
parkin_model = pkl.load(open("parkinson_pred.pkl", 'rb'))
kidney_model = pkl.load(open("kidney.pkl", 'rb'))
liver_model = pkl.load(open("live.pkl",'rb'))

if disease == "Parkinson's Disease":
    st.header("Parkinson Disease Prediction")
    Fo = st.number_input("MDVP:Fo(Hz)")
    Fhi = st.number_input("MDVP:Fhi(Hz)")
    Flo = st.number_input("MDVP:Flo(Hz)")
    Jitter = st.number_input("MDVP:Jitter(%)")
    Shimmer = st.number_input("MDVP:Shimmer")
    if st.button("Predict Parkinson Disease"):
        input_data = np.array([[Fo, Fhi, Flo, Jitter, Shimmer]])
        prediction = parkin_model.predict(input_data)

        if prediction[0]==1:
            st.error("You have Parkinson Disease")
        else:
            st.error("Negative")

elif disease == "Kidney Disease":
    st.header("Kidney Disease Prediction")
    age = st.number_input("Age")
    bp = st.number_input("Blood pressure")
    sg = st.number_input("Specific Gravity")
    al = st.number_input("Albumin")
    su = st.number_input("sugar")
    if st.button("Predict"):
        input_data = np.array(["age","bp","sg", "al","su"])
        prediction = kidney_model.predict(input_data)
        if prediction[0] == 1:
            st.error("You have Kidney Disease")
        else:
            st.error("Negative")
elif disease == "Liver Disease":
    st.header("Liver Disease Prediction")
    Age = st.number_input("Enter Age")
    Total_bilirubin = st.number_input("Total Bilirubin")
    Direct_Bilirubin = st.number_input("direct Bilirubin")
    Alkaline_Phosphotase = st.number_input("Alkaline Phosphotase")
    Alamine_Aminotransferase = st.number_input("Alamine Aminotransferase")
    if st.button("Predict"):
        input_data = np.array([Age, Total_bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase])
        prediction = liver_model.predict(input_data)
        if prediction == 1:
            st.error("You have Liver Disease")
        else:
            st.error("Negative")
st.markdown("------")