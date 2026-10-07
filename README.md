# 🤖 AI Chat Assistant

A beginner-friendly LLM application built with **Python, OpenAI Responses API and Streamlit**.

## Module 3 Coverage

This project demonstrates:

- LLM API integration using Python
- API-key authentication
- Environment variables and `.env`
- System/developer instructions
- User and assistant messages
- Conversation history
- Bounded history for basic token/cost management
- Configurable model and output-token limit
- Basic error handling
- Interactive Streamlit UI
- GitHub-ready project structure
- Streamlit Community Cloud deployment

## Project Structure

```text
ai-chat-assistant/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Create `.env`

Copy `.env.example` to `.env` and add your OpenAI API key:

```text
OPENAI_API_KEY=your_real_key
OPENAI_MODEL=gpt-6-luna
```

**Do not upload `.env` to GitHub.**

### 3. Start the app

```bash
streamlit run app.py
```

The terminal will provide a local Streamlit address.

## How the Application Works

1. The user enters a question.
2. Streamlit stores the conversation in `st.session_state`.
3. The application sends recent conversation history plus custom instructions to the LLM.
4. The OpenAI Responses API generates the assistant response.
5. The response is displayed in the chat interface.
6. Only a bounded number of recent messages are sent, helping reduce unnecessary token usage.

## Error Handling

The API call is wrapped in `try/except` so that authentication, model-access, network, or other API failures do not crash the application.

## Basic Cost Management

The application uses:

- a bounded conversation history,
- a configurable maximum output-token limit,
- a model selected through configuration.

These controls reduce unnecessary token usage. Actual API cost depends on the selected model and usage.

## Deployment

This project can be deployed using Streamlit Community Cloud from a GitHub repository.

For deployment, add the API key as a Streamlit secret rather than committing `.env`.

Example secret:

```toml
OPENAI_API_KEY = "your_real_key"
OPENAI_MODEL = "gpt-6-luna"
```

## Learning Outcome

By completing this project, the learner practices LLM APIs, authentication, environment variables, conversation management, custom instructions, error handling, token/cost awareness and basic AI application development.
