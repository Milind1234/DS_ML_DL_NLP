import streamlit as st 
import pandas as pd
import numpy as np

# Title of the application
st.title("hello Streamlit app")

st.write("This is a simple text")

df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column' : [10,20,30,40]
})

st.write("here is the dataframe")
st.write(df)

char_data = pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.line_chart(char_data)