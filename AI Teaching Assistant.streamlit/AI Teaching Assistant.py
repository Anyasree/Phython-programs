import streamlit as st
from google import genai
from google.genai import types
import config
client = genai.Client(api_key= config.GEMINI_API_KEY)

def generate_response(prompt, temperature=0.3):
    try:
        contents = [types.Content(role ="user", parts=[types.Part.from_text(text=prompt)])]
        config_params = types.GenerateContentConfig(temperature=temperature)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=contents, config=config_params)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
def setup_ui():
    st.title("AI Teaching Assistant")
    st.write("Welcome! You can ask me anything about various subjects, and I'll provide an answer.")
    user_input = st.text_input("Enter your question here:")
    if user_input:
        st.write(f"**Your question:** {user_input}")
        response = generate_response(user_input)
        st.write(f"**AI's answer:** {response}")
    else:
        st.write("Please enter a question to ask.")
def main():
    setup_ui()
if __name__ == "__main__":
    main()
