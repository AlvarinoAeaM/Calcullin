import openai
import streamlit as st

st.title("ChatBot-Calcullin")

# Coloca tu clave de API directamente aquí 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


# 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
# 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
openai.api_key = "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"

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Calculo Integral? Preguntame!!!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})