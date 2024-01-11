import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import joblib

df = pd.read_csv("../data/winequality-red.csv")

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df.iloc[:, :-1])
desired_clusters = 6
kmeans_model = KMeans(n_clusters=desired_clusters, n_init=10, random_state=42)
df['cluster'] = kmeans_model.fit_predict(scaled_data)

joblib.dump(scaler, "../joblib/scaler.joblib")
joblib.dump(kmeans_model, "../joblib/kmeans_model.joblib")