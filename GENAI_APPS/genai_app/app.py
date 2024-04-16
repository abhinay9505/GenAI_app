from openai import OpenAI
import streamlit as st
f = open(r"C:\Users\Abinay Rachakonda\Desktop\GENAI_APPS\app_keys\openai_key.txt")
key = f.read()
client = OpenAI(api_key=key)

st.title("AI MCQ Generator")
st.subheader("soom to be a Billion Dollor App Idea")

prompt = st.text_input("Enter the Data science Topic")


if st.button("Genrate")== True:
    st.balloons()
    response = client.chat.completions.create(                   
               model="gpt-3.5-turbo",
               messages=[
               {"role": "system", "content": """ YOU are helpfull AI Assistant
                                           
                GIVEN DATA SCIENCE topic you always genarat 3MCQ questions and answers for test.                                   
                """},
               {"role": "user", "content": prompt}
               ]
    )

st.write(response.choices[0].message.content)