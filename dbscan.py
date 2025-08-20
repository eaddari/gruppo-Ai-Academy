import pandas as pd
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt


df = pd.read_csv("20_08/dataset/Online_Retail_with_clv2.csv")
df.dropna(inplace=True)

db = DBSCAN(eps=0.5, min_samples=5)

db.fit_predict(df[["purchase_frequency", "CLV"]])
df['cluster'] = db.labels_

###### PLOT DBSCAN ######

plt.figure(figsize=(10, 6))
plt.scatter(df['purchase_frequency'], df['CLV'], c=df['cluster'], cmap='viridis', alpha=0.5)
plt.title("DBSCAN Clustering")
plt.xlabel("Purchase Frequency")
plt.ylabel("CLV")
plt.colorbar(label="Cluster")
plt.savefig("dbscan_purchase_frequency_clv.png")
plt.show()

##### SILHOUETTE SCORE #######

df_no_noise = df[df['cluster'] != -1]

silhouette_score = df_no_noise.groupby('cluster').apply(lambda x: (x['CLV'] - x['CLV'].mean()) ** 2).mean()
print(f"Silhouette Score: {silhouette_score}")