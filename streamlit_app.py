import streamlit as st #streamlit acts as a front end, importing streamlit reduces lot of front end work.
import os #picking up env vars
from PIL import Image #pillow is a library used for image handling in python.
import google.generativeai as genai #should be imported to use google gemini
genai.configure(api_key="AIzaSyBaRG02Kk1L4yNbxTZfzyRVJ3J-WwyO51M") #config. #
#function to load gemini pro vision
model=genai.GenerativeModel('gemini-1.5-flash')
def get_gemini_response(Input,Image,prompt):
    response=model.generate_content((Input,Image[0],prompt))
    return response.text
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("no file uploaded")
    
st.set_page_config(page_title="WIE's Invoice Generator")
st.sidebar.header("Aaruficial_Intelligence")
st.sidebar.write("Made By aarushi")
st.sidebar.write("Powered by google gemini ai")
st.header("Aaruficial_Intelligence")
st.subheader("Made By aarushi")
st.subheader("Manage your expenses with with Aaruficial_Intelligence")
input = st.text_input("What do you want me to do?",key="input")
uploaded_file = st.file_uploader("Choose an image",type=["jpg","jpeg","png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True) #indentation

ssubmit = st.button("Lets Go!")

input_prompt = """"
You are an expert in solving limits. I will upload an image, read the question, solve it, give me the answer and show the steps cutiepie.
At the end, make sure to repeat the name of my app "Aaruficial_Intelligence" and ask the user to use it again.
"""
if ssubmit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("Here's what you need to know")
    st.write(response)
