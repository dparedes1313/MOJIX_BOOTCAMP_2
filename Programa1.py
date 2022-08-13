import streamlit as st   
st.title("10 Cool Beginner Python Tricks That Will Make Your Life Easier") 
st.header ("Simple but effective tips for every python lovers")
st.image ('https://miro.medium.com/max/700/1*5IFgojJ4nU8f0YKTcjWDrg.jpeg')
st.caption("<h4 style='text-align: center;'>Photo by Miesha Maiden from Pexels</h4>", unsafe_allow_html=True)
st.write("<h4 style='text-align: center;'>Photo by Miesha Maiden from Pexels</h4>", unsafe_allow_html=True)
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
import pandas as pd
import numpy as np
import altair as alt

df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')
st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)