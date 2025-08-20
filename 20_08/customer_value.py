import pandas as pd

df = pd.read_csv("20_08/dataset/Online_Retail_cleaned.csv")

def customer_value(df):

    df = df.copy()

    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    clv_df = df.groupby('CustomerID').agg({
        'TotalPrice': 'sum',
        'InvoiceNo': 'nunique',
        'InvoiceDate': ["min", "max"]
    })
    clv_df.columns = ['TotalRevenue', 'NumPurchases', 'FirstPurchase', 'LastPurchase']

    clv_df['Years'] = (clv_df['LastPurchase'] - clv_df['FirstPurchase']).dt.days / 365
    clv_df['Years'] = clv_df['Years'].replace(0, 1)

    clv_df['Frequency'] = clv_df['NumPurchases'] / clv_df['Years']

    clv_df['AvgOrderValue'] = clv_df['TotalRevenue'] / clv_df['NumPurchases']

    clv_df['CLV'] = clv_df['AvgOrderValue'] * clv_df['Frequency'] * clv_df['Years']

    print(clv_df[['CLV']].sort_values(by='CLV', ascending=False).head(10))
    print(f"CLV media: {clv_df['CLV'].mean():.2f}")

    df['CLV'] = df['CustomerID'].map(clv_df['CLV'])

    return df