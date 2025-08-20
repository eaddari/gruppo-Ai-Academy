import pandas as pd

df = pd.read_csv("20_08/dataset/Online_Retail.csv", 
                 sep=",",            # separatore corretto
                 encoding="latin1",  # evita errori Unicode
                 quotechar='"')      # gestisce le virgolette nei campi testo

print(df.head())
print(df.info())