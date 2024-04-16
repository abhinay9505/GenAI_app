from openai import OpenAI
import streamlit as st

st.title("A Code Correction using Gen AI")

prompt = st.text_input("ENTER THE INPUT")

f = open(r"C:\Users\Abinay Rachakonda\Desktop\GENAI_APPS\app_keys\openai_key.txt")

OPENAI_API_KEY = f.read()

client = OpenAI(api_key = OPENAI_API_KEY)

def chat_bot(prompt):
    response = client.chat.completions.create(
                      model="gpt-3.5-turbo",
                      messages=[
                        {"role": "system", "content": """You are a teaching assistant for students .. 
                         you are need to explain and fix the bugs and explain student where he is done mistakes
                                        """},
                        {"role": "user", "content": prompt}
                      ]
                )
    return response.choices[0].message.content
if st.button("fixing code"):

    st.write(chat_bot(prompt))