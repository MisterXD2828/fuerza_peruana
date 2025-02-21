from groq import Groq
import streamlit as st

client = Groq(
    api_key = "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",
)

pregunta = st.chat_input("Qué quieres saber?")
if pregunta:
    with st.chat_message("user"):
        st.write(pregunta)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": pregunta,
            }
        ],
        model="llama3-8b-8192",
    )
    with st.chat_message("ai"):
        st.write(chat_completion.choices[0].message.content)