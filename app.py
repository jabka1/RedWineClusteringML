from flask import Flask, render_template, request
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

app = Flask(__name__)

kmeans_model = joblib.load("joblib/kmeans_model.joblib")
scaler = joblib.load("joblib/scaler.joblib")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        fixed_acidity = float(request.form['fixed_acidity'])
        volatile_acidity = float(request.form['volatile_acidity'])
        citric_acid = float(request.form['citric_acid'])
        residual_sugar = float(request.form['residual_sugar'])
        chlorides = float(request.form['chlorides'])
        free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
        total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
        density = float(request.form['density'])
        pH = float(request.form['pH'])
        sulfates = float(request.form['sulphates'])
        alcohol = float(request.form['alcohol'])

        user_data = scaler.transform([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulfates, alcohol]])
        cluster = int(kmeans_model.predict(user_data)[0])
        predicted_quality = cluster
        return render_template('index.html', cluster=predicted_quality)

if __name__ == '__main__':
    app.run(debug=True)
