import os

import pandas as pd
from sklearn.discriminant_analysis import StandardScaler



DATASET_PATH = os.path.join(os.path.dirname(__file__), "dataset", "Online_Retail.csv")

CLEANED_DATASET_PATH = os.path.join(os.path.dirname(__file__), "dataset", "Online_Retail_cleaned.csv")

df = pd.read_csv(
    DATASET_PATH,
    sep=",",
    encoding="latin1",
    quotechar='"',
)

print(df.head())
print(df.info())


df.dropna(subset=["CustomerID"], inplace=True)

df = df[(df["Quantity"] > 0) & (df["Quantity"] < 13)]

df = df[(df["UnitPrice"] >= 0.01) & (df["UnitPrice"] < 10)]

scaler = StandardScaler()
df[["Quantity", "UnitPrice"]] = scaler.fit_transform(df[["Quantity", "UnitPrice"]])

df.drop(columns=["StockCode", "Description"], inplace=True)

df.to_csv(CLEANED_DATASET_PATH, index=False)