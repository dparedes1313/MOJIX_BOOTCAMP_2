import streamlit as st
####SIDE BAR ################################################################# 
st.sidebar.title("100 Cool Beginner Python Tricks That Will Make Your Life Easier")

st.sidebar.title("Contact")
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)
####MAIN PAGE #################################################################
##### CARGA DE DATOS CSV ##############################
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
     # To read file as bytes:
     bytes_data = uploaded_file.getvalue()
     st.sidebar.write(bytes_data)

     # To convert to a string based IO:
     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
     st.sidebar.write(stringio)

     # To read file as string:
     string_data = stringio.read()
     st.sidebar.write(string_data)

     # Can be used wherever a "file-like" object is accepted:
     dataframe = pd.read_csv(uploaded_file)
     st.sidebar.write(dataframe)
###################################################################