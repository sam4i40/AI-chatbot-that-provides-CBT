#import required libraries

import openai
import streamlit as st
from streamlit_chat import message

#set the GPT-3 api key
openai.api_key = st.secrets['pass']

st.header("MON - your AI friend");

def generate_response(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature=0.5,
    )
    if prompt == "hi" or prompt == "Hi" or prompt == "hello" or prompt == "Hello" : message = "Hi. How can I help you?"
    else : message = completions.choices[0].text
    return message

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("", key="input")
    return input_text

user_input = get_text()

if user_input:
    output = generate_response(user_input)
    # store the output 
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://i.ibb.co/4sxNzxq/background.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )