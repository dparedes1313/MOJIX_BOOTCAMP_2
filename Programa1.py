import streamlit as st   
st.title("10 Cool Beginner Python Tricks That Will Make Your Life Easier") 
st.header ("Simple but effective tips for every python lovers")
st.image ('https://miro.medium.com/max/700/1*5IFgojJ4nU8f0YKTcjWDrg.jpeg')
st.caption("<h4 style='text-align: center';'>Photo by Miesha Maiden from Pexels</h4>", unsafe_allow_html=True)
st.write("<h2><p>The compactness of Python can make a developer&rsquo;s life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can surprise you with their amazing capabilities.</p></h2>", unsafe_allow_html=True)
st.write("<h2><p>In today’s article, I will discuss 10 Python tips and tricks that will be really helpful for beginners to write more compact code. Knowing these tips and tricks will definitely save you some valuable time.</p></h2>", unsafe_allow_html=True)
st.header('1. Walrus operator')
st.write("<h2><p>The&nbsp;<code><strong>Walrus</strong></code><strong>&nbsp;or&nbsp;</strong><code><strong>:=</strong></code>&nbsp;operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.</p></h2>", unsafe_allow_html=True)
st.header('Example')
st.write("<h2><p>If we want to check and print the length of a list:</p></h2>", unsafe_allow_html=True)
st.code("Mylist = [1,2,3]")
st.code("if(l := len(mylist) &gt; 2)")
st.code("print(l)")
st.write("<h2><p>Output</p></h2>", unsafe_allow_html=True)
st.code("3")




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