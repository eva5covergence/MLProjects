from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

load_dotenv()
glg_key = "AIzaSyDAxRyIdME7kMRCxrfKdtChItZaQIA7D_4"
genai.configure(api_key=glg_key)
model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input,image,prompt):
    response = model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{
            "mime_type":uploaded_file.type,
            "data": bytes_data
        }]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

st.set_page_config(page_title="Prescription reader")
st.header("Medical Prescription Extractor")
question = st.text_input("question about prescription: ",key="input")
uploaded_file = st.file_uploader("Upload your prescription...",type=['jpg','jpeg','png'])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded prescription.", use_column_width=True)

submit = st.button("Tell me about the prescription")
input_prompt="""
You are an expert in understanding hand written medical prescription. 
we will upload a image as medical prescription and you will have to answer any questions based on the uploaded prescription image"""

if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt,image_data,question)
    st.subheader("The Response is:")
    st.write(response)




