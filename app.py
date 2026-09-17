import streamlit as st
import pandas as pd
import joblib

model = joblib.load("insurance_model.pkl")
model_columns = joblib.load("model_columns.pkl")

st.set_page_config(page_title="Medical Insurance Cost Predictor", page_icon="download.png")
st.title("Medical Insurance Cost Predictor")
st.write("Enter the details below to estimate the medical insurance cost.")
col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=30, step=1)
    bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0, step=0.1)
    children = st.number_input("Number of Children", min_value=0, max_value=10, value=0, step=1)
with col2:
    sex = st.selectbox("Gender", ["male", "female"])
    smoker = st.selectbox("Smoking Status", ["yes", "no"])
    region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

if st.button("Predict Insurance Cost"):
    input_df = pd.DataFrame({
        "age": [age],
        "bmi": [bmi],
        "children": [children],
        "sex": [sex],
        "smoker": [smoker],
        "region": [region],
    })

    input_encoded = pd.get_dummies(input_df)
    input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)
    prediction = model.predict(input_encoded)[0]
    st.success(f"### Estimated Insurance Cost: ${prediction:,.2f}")

    with st.expander("See input summary"):
        st.write(input_df)