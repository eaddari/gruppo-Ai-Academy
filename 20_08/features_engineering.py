import os
import pandas as pd
from sklearn.discriminant_analysis import StandardScaler

DATASET_PATH = os.path.join(os.path.dirname(__file__), "dataset", "Online_Retail_with_clv.csv")

df = pd.read_csv(
    DATASET_PATH,
    sep=",",
    encoding="latin1",
    quotechar='"',
)

df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

features = df.groupby("CustomerID").agg(
    total_quantity=("Quantity", "sum"),
    total_spent=("TotalPrice", "sum"),
    avg_spent=("TotalPrice", "mean"),
    purchase_frequency=("InvoiceNo", "nunique")
).reset_index()

scaler = StandardScaler()
num_cols = ["total_quantity", "total_spent", "avg_spent", "purchase_frequency", "CLV"]

df = pd.concat([df, features], axis=1)

df[num_cols] = scaler.fit_transform(df[num_cols])

df.to_csv("20_08/dataset/Online_Retail_with_clv2.csv", index=False)

