import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib


feature_names = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar',
                  'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density',
                  'pH', 'sulphates', 'alcohol']

st.title('Wine Quality Clustering')

user_input = {}
for feature in feature_names:
    value = st.text_input(f'Enter {feature}', value='0.0')
    try:
        value = float(value.replace(',', '.'))
    except ValueError:
        st.error(f"Invalid input for {feature}. Please enter a valid numerical value.")
        st.stop()
    user_input[feature] = value

user_data = pd.DataFrame([user_input], dtype=float)

scaler = joblib.load("../joblib/scaler.joblib")
kmeans_model = joblib.load("../joblib/kmeans_model.joblib")

scaled_user_data = scaler.transform(user_data)

predicted_cluster = kmeans_model.predict(scaled_user_data)[0]

st.header(f"Cluster: {predicted_cluster}")