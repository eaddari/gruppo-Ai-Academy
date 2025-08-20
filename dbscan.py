
import pandas as pd
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score


db = DBSCAN(eps=0.5, min_samples=5)
db.fit_predict(df[["CustomerID", "CLV"]])
df['cluster'] = db.labels_

df = pd.read_csv("20_08/dataset/Online_Retail_with_clv.csv")

# One-hot encoding della colonna Country
df_encoded = pd.get_dummies(df, columns=["Country"])

# DBSCAN su CustomerID, CLV e Country one-hot
features = ["CustomerID", "CLV"] + [col for col in df_encoded.columns if col.startswith("Country_")]
db = DBSCAN(eps=0.5, min_samples=5)
db.fit_predict(df_encoded[features])
df['cluster'] = db.labels_

###### PLOT DBSCAN ######

plt.figure(figsize=(10, 6))
plt.scatter(df['CustomerID'], df['CLV'], c=df['cluster'], cmap='viridis', alpha=0.5)
plt.title("DBSCAN Clustering")
plt.xlabel("CustomerID")
plt.ylabel("CLV")
plt.colorbar(label="Cluster")
plt.savefig("dbscan_customer_clv.png")
plt.show()

df_no_noise = df[df['cluster'] != -1]
silhouette_score = df_no_noise.groupby('cluster').apply(

##### SILHOUETTE SCORE #######
mask = df['cluster'] != -1

if df['cluster'][mask].nunique() > 1:
    score = silhouette_score(df_encoded.loc[mask, features], df.loc[mask, 'cluster'])
    print(f"Silhouette Score: {score:.2f}")
else:
    print("Silhouette score cannot be computed: less than 2 clusters (excluding noise).")


db2 = DBSCAN(eps=0.5, min_samples=5)
db2.fit_predict(df[["Country", "CLV"]])
df['cluster'] = db2.labels_

###### PLOT DBSCAN ######

plt.figure(figsize=(10, 6))
plt.scatter(df['Country'], df['CLV'], c=df['cluster'], cmap='viridis', alpha=0.5)
plt.title("DBSCAN Clustering")
plt.xlabel("Country")
plt.ylabel("CLV")
plt.colorbar(label="Cluster")
plt.savefig("dbscan_country_clv.png")
plt.show()

##### SILHOUETTE SCORE #######

df_no_noise = df[df['cluster'] != -1]

silhouette_score = df_no_noise.groupby('cluster').apply(
    lambda x: (x['CLV'] - x['CLV'].mean()) ** 2).mean()
print(f"Silhouette Score: {silhouette_score:.2f}")