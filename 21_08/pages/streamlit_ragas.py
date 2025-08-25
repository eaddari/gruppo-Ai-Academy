import streamlit as st
import os
import pandas as pd

st.set_page_config(
    page_title="ragas metrics",
    layout="wide"
)

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)

st.title("Ragas metrics")
st.dataframe(df)

