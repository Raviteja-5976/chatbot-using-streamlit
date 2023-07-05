#importing packages
import streamlit as st
import openai

#your openai API key
openai.api_key = 'YOUR OPENAI API KEY'

#taking input in a variable 
messages = [{"role": "system", "content": " "}]

#sending the query and receving the reply from openai
def text_message(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

#title of the page
st.title('MINE')

#input space
user_input = st.text_input("User Input")

#to write the output
if user_input:
    reply = text_message(user_input)
    st.write(f"*[Bot]:* {reply}")
