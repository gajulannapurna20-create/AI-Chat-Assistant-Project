import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 AI Chat Assistant")
st.caption("LLM API application built with Python, OpenAI Responses API and Streamlit.")

# ---------- Configuration ----------
api_key = os.getenv("OPENAI_API_KEY")
default_model = os.getenv("OPENAI_MODEL", "gpt-6-luna")

# Streamlit Community Cloud secrets fallback.
if not api_key:
    try:
        api_key = st.secrets.get("OPENAI_API_KEY")
        default_model = st.secrets.get("OPENAI_MODEL", default_model)
    except Exception:
        pass

with st.sidebar:
    st.header("⚙️ Settings")
    model = st.text_input("Model", value=default_model)
    instructions = st.text_area(
        "Custom instructions",
        value=(
            "You are a helpful, clear and friendly AI assistant. "
            "Explain concepts in simple language and use examples when useful."
        ),
        height=130,
    )
    max_output_tokens = st.slider(
        "Maximum output tokens",
        min_value=100,
        max_value=1200,
        value=600,
        step=100,
        help="Lower limits help control API usage and cost.",
    )

    if st.button("🗑️ Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

if not api_key:
    st.warning(
        "OPENAI_API_KEY is not configured. Add it to your local .env file "
        "or to Streamlit Community Cloud Secrets before using the assistant."
    )
    st.stop()

client = OpenAI(api_key=api_key)

# ---------- Conversation history ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------- User input ----------
prompt = st.chat_input("Ask me anything...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Keep a bounded history to reduce unnecessary token usage.
    recent_messages = st.session_state.messages[-12:]

    input_items = [
        {"role": "developer", "content": instructions},
        *recent_messages,
    ]

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.responses.create(
                    model=model,
                    input=input_items,
                    max_output_tokens=max_output_tokens,
                )
                answer = response.output_text.strip()

                if not answer:
                    answer = "I couldn't generate a response. Please try again."

                st.markdown(answer)
                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )

            except Exception as exc:
                error_message = (
                    "Sorry, I couldn't complete that request. "
                    "Please check your API key, model name, internet connection, "
                    "and API account access."
                )
                st.error(error_message)
                # Keep technical details out of the public UI while preserving
                # a useful message for debugging in the terminal/logs.
                print(f"OpenAI API error: {type(exc).__name__}: {exc}")

st.divider()
st.caption("Built for Module 3: LLM APIs & Application Development")
