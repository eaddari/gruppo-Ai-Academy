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



# Creazione colonna valore totale
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Aggregazione per cliente con Paese
features = df.groupby("CustomerID").agg(
    total_quantity=("Quantity", "sum"),
    total_spent=("TotalPrice", "sum"),
    avg_spent=("TotalPrice", "mean"),
    purchase_frequency=("InvoiceNo", "nunique"),
    country=("Country", "first")  # Paese di appartenenza
).reset_index()

# Standardizzazione delle feature numeriche
scaler = StandardScaler()
num_cols = ["total_quantity", "total_spent", "avg_spent", "purchase_frequency"]
features[num_cols] = scaler.fit_transform(features[num_cols])

print(features.head())