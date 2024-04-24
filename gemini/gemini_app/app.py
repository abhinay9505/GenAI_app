import streamlit as st
import google.generativeai as gemini

st.set_page_config(page_title="conversationai", page_icon="🤖", layout="wide")

#s Define available languages and their corresponding models


list_languages = ['GeminiAi','prompt Engineering','Data science',
                  'Mathematics','Machine learning']
language = st.selectbox ("Select an AI Tutor ", list_languages)

st.title(f"🤖 {language}")

f = open(r"C:\Users\Abinay Rachakonda\Desktop\gemini\key\geminiai_key.txt")
api_key = f.read()

gemini.configure(api_key=api_key)
  # Get the corresponding model for the selected language
model = gemini.GenerativeModel(model_name="gemini-1.5-pro-latest",
                               system_instruction=f'''You are AI Assistant to {language}
                               Queries of the user.''')

if "messages" not in st.session_state.keys() or st.session_state.language != language:
    st.session_state.messages = [
        {"role": "assistant", "content": f"Hello, this is Gemini and how can I help you with {language} today?"}
    ]
    st.session_state.language = language
    st.title(f"📢:red[How may I help you with {language} today?]")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input()

if user_input is not None:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Loading..."):
            ai_response = model.generate_content(user_input)
            st.write(ai_response.text)
    new_ai_message = {"role": "assistant", "content": ai_response.text}
    st.session_state.messages.append(new_ai_message)