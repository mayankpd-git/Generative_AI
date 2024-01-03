import streamlit as st
from dotenv import load_dotenv
from utils import query_agent
import os

os.environ["OPENAI_API_KEY"] = "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"

load_dotenv()

st.title('CSV Explorer')
st.header('Upload your CSV file')
data = st.file_uploader('Upload CSV file', type='csv')

query = st.text_area('Enter your Query')
button = st.button('Generate')

if button:
    answer = query_agent(data, query)
    st.write(answer)