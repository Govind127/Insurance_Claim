#Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import seaborn as sns

#Loading Data
df = pd.read_csv('/content/insurance_data - insurance_data - insurance_data - insurance_data.csv')
df.head()

from sklearn.preprocessing import StandardScaler, MinMaxScaler
scaler_standard = StandardScaler()
standard_scaled = scaler_standard.fit_transform(df)

#Seprate features and target
X = df[['age','affordibility']]
y = df['bought_insurance']

#Train, Test and Split the Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


#Perfroming K-Means Clustering
from sklearn.cluster import KMeans

#Using Age and Affordability for Clustering
X = df[['age', 'affordibility']]

# Step 1: Fit the model
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)

#Adding cluster labels to the DataFrame
df['cluster'] = kmeans.labels_

#Visualize the clusters
plt.figure(figsize=(8,5))
plt.scatter(df['age'], df['affordibility'], c=df['cluster'], cmap='viridis', s=100, edgecolors='k')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], c='red', s=200, marker='X', label='Centroids')
plt.xlabel("Age")
plt.ylabel("Affordibility")
plt.title("K-Means Clustering (K=2)")
plt.legend()
plt.grid(True)
plt.show()

# Determine optimal K
sse = []  # Sum of Squared Errors

for k in range(1, 10):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X)
    sse.append(km.inertia_)  # Inertia = SSE

plt.plot(range(1, 10), sse, marker='o')
plt.xlabel("Number of Clusters (K)")
plt.ylabel("SSE (Inertia)")
plt.title("Elbow Method for Optimal K")
plt.grid(True)
plt.show()
