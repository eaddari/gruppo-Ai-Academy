import os

import pandas as pd

DATASET_PATH = os.path.join(os.path.dirname(__file__), "dataset", "Online_Retail.csv")

df = pd.read_csv(
    DATASET_PATH,
    sep=",",  # separatore corretto
    encoding="latin1",  # evita errori Unicode
    quotechar='"',
)  # gestisce le virgolette nei campi testo

print(df.head())
print(df.info())
