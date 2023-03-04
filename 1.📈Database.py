import streamlit as st 
import pandas as pd
import numpy as np
import graphviz as graphviz
import plotly.express as px


st.title("Database")
from PIL import Image
img =Image.open("C:\PYTHON\Streamlit Python\Multiple page\Screenshot 2023-03-04 104317.png")
img =img.convert('RGB')
st.image(img,width=1000)
st.title("Workclass")
df = pd.DataFrame(
    np.random.randn(10,2),
    columns=['privat','Goverment']
)
st.area_chart(df)
st.title("Salary")
df = pd.DataFrame(
    np.random.randn(10,2),
    columns=['>=50k','<50k']
)
st.bar_chart(df)
st.title("Sex")
df= pd.DataFrame( 
       np.random.randn(8, 2), 
             columns=['male', 'female'])
st.line_chart(df)

st.title("Race")
df= pd.DataFrame( 
       np.random.randn(5, 2), 
             columns=['Black', 'White'])
st.area_chart(df)


st.graphviz_chart('''
digraph{
    Start -> Data_Collection
    Data_Collection -> Post_Entries_to_Journal 
    Post_Entries_to_Journal ->  Post_Entries_to_Ledger_Accounts
    Post_Entries_to_Ledger_Accounts -> Adjusted_Trial_Balance
    Adjusted_Trial_Balance -> Prepare_Financial_Satement
    Prepare_Financial_Satement -> Financial_Statement
     }
''')


