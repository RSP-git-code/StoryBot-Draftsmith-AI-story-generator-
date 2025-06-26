import streamlit as st
import openai
import time
#  Page Setup 
st.set_page_config(page_title="📚 StoryBot Draftsmith", layout="centered")
#Title of the Webpage or app
st.title("📚 StoryBot Draftsmith")
#Description
st.write("Your AI partner-in-crime for writing amazing stories ✍️")

#  OpenAI API key 
openai.api_key = ""  # Use only your api key
# Initialize chat history in session state 
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a creative storyteller AI. Continue the story based on previous conversation unless the user says to start over."}
    ]

# Display full chat history 
#Doesnt repeat what chatbot responded again to avoid confusion
for msg in st.session_state.messages[1:]:  
    # provides role like user or bot
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input 
if prompt := st.chat_input("Continue the story or give a new idea..."):
    # Append user's message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("⏳ Drafting your story.Please wait"):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  
                messages=st.session_state.messages,
                temperature=0.8
            )
            reply = response.choices[0].message["content"]
            time.sleep(1)
            st.markdown(reply)

    # Append assistant response to session state
    st.session_state.messages.append({"role": "assistant", "content": reply})
