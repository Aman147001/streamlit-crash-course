# https://www.youtube.com/watch?v=d7fnzDQ5qM8
# github.com/streamlit/app-starter-kit

import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello world!")

with st.sidebar:
    st.header("About app")
    st.write("This is my first app!")


st.header("This is a header with a divider", divider="rainbow")
st.header(':red[**Streamlit**] is :blue[cool] :sunglasses:')

st.markdown("This is created using markdown.")

x = st.slider("Choose an x value", 1, 20)
x
st.write("The value of :blue[***x***] is:", x)

st.subheader("st.columns")
col1, col2 = st.columns((4,6))
with col1:
    y = st.slider("Choose a y value", 0, 20)
with col2:
    st.write("The value of :orange[***y***] is:", y)

st.subheader("st.area_chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)
