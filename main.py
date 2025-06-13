#https://medium.com/@whyamit101/streamlit-bar-chart-a-practical-guide-for-beginners-c7403008f43f

import streamlit as st
import pandas as pd

data = {
    'Fruits': ['Apples', 'Bananas', 'Cherries', 'Dates'],
    'Sales DE' : [65, 65, 20, 10],
    'Sales FR': [55, 75, 30, 45]
}
df = pd.DataFrame(data)

st.title('Sales by Fruits')
st.bar_chart(df.set_index('Fruits'))