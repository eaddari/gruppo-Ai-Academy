import pandas as pd
from customer_value import customer_value

df = pd.read_csv("20_08/dataset/Online_Retail_cleaned.csv")

df = customer_value(df)

df.to_csv("20_08/dataset/Online_Retail_with_clv.csv", index=False)
