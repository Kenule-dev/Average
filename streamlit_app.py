import streamlit as st
import pandas as pd
st.title('My machine learning app')

st.info('My first ML app')

url='https://raw.githubusercontent.com/Kenule-dev/Average/refs/heads/master/Exam_Score_Prediction.csv'
df=pd.read_csv(url)
df
