import streamlit as st   
st.title("10 Cool Beginner Python Tricks That Will Make Your Life Easier") 
st.subheader ("Simple but effective tips for every python lovers")
st.image ('https://miro.medium.com/max/700/1*5IFgojJ4nU8f0YKTcjWDrg.jpeg')
st.caption("The compactness of Python can make a developer’s life")

st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")

st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')
st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)