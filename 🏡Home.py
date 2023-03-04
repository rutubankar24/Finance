import streamlit as st  
import pandas as pd  
st.set_page_config(
    page_title="multipage App",
    page_icon="👋",
)
st.title("🔹Project Title:")
st.text('''Adult Census Income Prediction''')
st.title("🔹Technologies:")
st.text('''Machine Learning Technology''')
st.title("🔹Domain:")
st.text('''Finance''')
st.button("Customer Info")
Name = st.text_input("Enter Your Name")
st.slider("What Is your Age",12,70)
Contact = st.text_input("Contact No📲")
Gmail = st.text_input("Enter your Gmail ID")
st.selectbox("Gender",['','Male🧔','Female🧔'])
st.selectbox("Marital status",['','Married👫','Unmarried🧍🧍'])
Address = st.text_input("Enter Your Address🏡")
st.selectbox("Enter Your Workclass🏢",['','Private','Goverment'])
Education = st.text_input("Education🎓")
st.selectbox("Enter Your Salary💷",['','50k','>50k','<50k'])
st.slider("Loan",15000,5000000)
Info = st.text_input("Why you need a loan")
Start = st.date_input("Date of loan taken by you")
End = st.date_input("The date on which you have to repay the loan")
uploaded_file = st.file_uploader("Upload Your Photo")
