# Streamlit Package for Interface
import streamlit as st
# Openai package for the text generation and also the Inage generation
import openai

#TITLE
st.title('MINE-GPT')
st.subheader('by Raviteja')

# CREATING TABS
tab1, tab2 = st.tabs(["ASK AI","GENERATE IMAGE WITH AI"])

# OPENAI APIKEY
openai.api_key = '<YOUR OPENAI API KEY>'



# CREATING TAB-1
with tab1:
    st.title('ASK AI')
    st.caption('NOTE: The server might overload and give ERROR, If that happens please close the website and open again')

    # SENDING QUERY TO OPENAI
    messages = [{"role": "system", "content": "Act like Your name is MINE and Not ChatGPT."}]

    def text_message(user_input):
        messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
        )
        # GETTING RESPONCE
        ChatGPT_reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": ChatGPT_reply})
        return ChatGPT_reply

    # USER INPUT TEXT BOX
    user_input = st.text_input("User Input :")
    
    st.write('Clear your text box to type in the next question') 

    #CREATING THE BUTTON
    if st.button('Enter'):  #IF YOU CLICK THE BUTTION THEN RUN CODE BELOW
        # st.write('Your Question')
        # st.write(user_input)
        reply = text_message(user_input)
        st.write(f"*[Bot]:* {reply}")
    st.caption('This is a AI bot which answers the questions you asked (anything you want to ask)')
    st.caption('TIP: The more spefic the question, the more accurate the answer given by the bot')

# CREATING TAB-2
with tab2:
    st.title('IMAGE GENERATION')
    st.caption('NOTE: The server might overload and give ERROR, If that happens please close the website and open again')

    # CREATING THE TEXT BOX
    PROMPT = st.text_input('Enter Your Creative Prompt :')
    st.write('Clear your text box to type in the next question')     

    # YOUR OPENAI API KEY
    openai.api_key = '<YOUR OPENAI API KEY>'

    
    if st.button('Generate Your Creative Image'):  # IF YOU CLICK THE BUTTON THEN RUN THE CODE BELOW
        # SENDING THE PROMPT AND GETTING THE RESPONCE 
        response = openai.Image.create(
            prompt=PROMPT,
            n=1,  # CREATE ONLY ONE IMAGE
            size="256x256",  # CREATE SIZE OF 256X256 OR 512X512 OR 1024X1024
        )

        # GETTING THE RESPONCE FROM OPENAI AND DISPLAYING IT USING STREAMLIT
        gen=response["data"][0]["url"]  # THE [0] MEAN TO DISPLAY THE FIRST IMAGE, YOU CAN ADD MORE
        st.image(gen,caption=PROMPT)
    
    st.caption('This is an AI image generator, you can specify anuthing you want and it will generate(Even if it does not exist or physically impossible)')
    st.caption('TIP: Try to be creative and as specific as possible')
