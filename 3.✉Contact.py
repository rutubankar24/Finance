import streamlit as st
import pandas as pd
import time
st.title("Information")
from PIL import Image
img =Image.open("C:\PYTHON\Streamlit Python\Multiple page\Round Photo_Jan222023_170116.png")
img =img.convert('RGB')
st.image(img,width=180)
st.title('🔹Name:')
st.text('Rutuja Bankar')
st.title('🔹Collage Name:')
st.text('NMIET,Talegaon,Pune')
st.title('🔹Education:')
st.text('ENTC Engineering')
st.title('🔹Mobile No:')
st.text('7709802074')
st.title('🔹Email Id:')
st.text('rutubankar24@gmail.com')
st.success("Thank You")
st.balloons()
time.sleep(10)
