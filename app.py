from dotenv import load_dotenv
load_dotenv() ## Loading all the environment variable

import streamlit as st
import os
import google.generativeai as genai 



#genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
api_key=st.secrets['GOOGLE_API_KEY']
## Function to load gemini pro model and get responses
if api_key:
    genai.configure(api_key=api_key)
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response= model.generate_content(question)
    return response.text

## Initialize our Streamlit app
st.set_page_config(page_title="ChatMaven")
st.header("ChatMavan")


input=st.text_input("Ask Me Anything",key="input")

## When submit is clicked



##submit button
submit=st.button("Click me!")

## Animated click button
button_css = st.markdown("""
<style>
@keyframes pulse {
  0% {
    transform: scale(0.95);
  }
  70% {
    transform: scale(1.05);
  }
  100% {
    transform: scale(0.95);
  }
}
.stButton>button {
  animation: pulse 2s infinite;
  font-size: 20px;
}
</style>
""", unsafe_allow_html=True)



if submit:
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)

    
