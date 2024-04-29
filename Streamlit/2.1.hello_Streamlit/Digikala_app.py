import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
st.title("Digikala App")
# Load data
with st.sidebar:
    st.image("https://github.com/MohamadNematizadeh/PyDeploy/blob/main/Streamlit/2.1.hello_Streamlit/imgae/Digikala-logo.png?raw=true", use_column_width=True)

    st.write("This App can get a complete data from Digikala and displays the sales details of Digikala products")

digikala = pd.read_csv("data/digikala-orders.csv")
digikala["DateTime_CartFinalize"] = pd.to_datetime(digikala["DateTime_CartFinalize"])
digikala["YearMonth"] = digikala["DateTime_CartFinalize"].dt.to_period('M')
digikala

orders = digikala.groupby("YearMonth")["Quantity_item"].sum().reset_index()
orders

x_axis = orders["YearMonth"].astype(str)
y_axis = orders["Quantity_item"]

st.title("Sales chart of Digikala products")
st.line_chart(data=orders, x="YearMonth", y='Quantity_item', use_container_width=True)
