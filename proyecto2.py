import streamlit as st
####SIDE BAR ################################################################# 
st.sidebar.title("100 Cool Beginner Python Tricks That Will Make Your Life Easier")
st.sidebar.header('1. Walrus operator')
st.sidebar.header('2. Splitting a string')
st.sidebar.header('3. Reversing a string')
st.sidebar.header('4. Merging two dictionaries')
st.sidebar.header('5.The zip() function')
st.sidebar.header('6. Assigning multiple list values to a variable')
st.sidebar.header('7. Remove duplicate list items')
st.sidebar.header('8. Lambda function')
st.sidebar.header('9. Swapping variable value')
st.sidebar.header('10. Use a password in your code')
     
st.sidebar.title("Contact")
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)
####MAIN PAGE #################################################################
##### CARGA DE DATOS CSV ##############################
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     # To read file as bytes:
     bytes_data = uploaded_file.getvalue()
     st.write(bytes_data)

     # To convert to a string based IO:
     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
     st.write(stringio)

     # To read file as string:
     string_data = stringio.read()
     st.write(string_data)

     # Can be used wherever a "file-like" object is accepted:
     dataframe = pd.read_csv(uploaded_file)
     st.write(dataframe)
###################################################################