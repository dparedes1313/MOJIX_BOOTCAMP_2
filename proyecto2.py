
import pandas as pd
import streamlit as st

st.title("Hello world!")

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
     bytes_data = uploaded_file.read()
     st.write("filename:", uploaded_file.name)
     st.write(bytes_data)
     
     df = pd.DataFrame(
     np.random.randn(50, 20),
     columns=('col %d' % i for i in range(20)))
     st.write(df)