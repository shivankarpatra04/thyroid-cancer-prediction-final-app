import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables and configure API
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize language model
llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.6)
output_parser = StrOutputParser()

# Define prompt templates
initial_prompt_template = ChatPromptTemplate.from_template("""
    Answer the question as detailed as possible from the provided context, make sure to provide all the details.
    If the answer is not in the provided context, respond with "ANSWER_NOT_AVAILABLE".
    Context: {context}
    Question: {question}
    """)

specialist_prompt_template = ChatPromptTemplate.from_template("""
    As a specialist in thyroid cancer, provide a comprehensive response based on your expertise in 40 to 50 words.
    Question: {question}
    """)

# Create chains
initial_chain = initial_prompt_template | llm | output_parser
specialist_chain = specialist_prompt_template | llm | output_parser

# Function to process response
def process_response(response, question):
    if response.startswith("ANSWER_NOT_AVAILABLE"):
        specialist_response = specialist_chain.invoke({"question": question})
        return f"The answer is not available in the given context. However, based on specialist knowledge:\n\n{specialist_response}"
    return response

# Load context from file
with open('q&a.txt', 'r', encoding='utf-8') as file:
    context = file.read()

# Streamlit app
st.title("Chat Assistant")

# Initialize session state for chat history if it doesn't exist
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Text input for question
question = st.text_input("Ask a question:")

if st.button("Get Answer"):
    if question:
        with st.spinner("Generating answer..."):
            inputs = {"context": context, "question": question}
            initial_response = initial_chain.invoke(inputs)
            processed_response = process_response(initial_response, question)
            st.write(processed_response)
            
            # Add current Q&A to history
            st.session_state.chat_history.append((question, processed_response))
    else:
        st.warning("Please enter a question.")

# Add a toggle for showing chat history
show_history = st.checkbox("Show Chat History")

# Display chat history if toggle is on
if show_history:
    st.subheader("Chat History")
    
    # Create a scrollable area using st.expander
    with st.expander("Chat History", expanded=True):
        # Reverse the chat history to show most recent at the top
        for i, (q, a) in enumerate(reversed(st.session_state.chat_history)):
            st.markdown(f"**Q{len(st.session_state.chat_history)-i}:** {q}")
            st.markdown(f"**A{len(st.session_state.chat_history)-i}:** {a}")
            st.markdown("---")  # Add a separator between Q&A pairs

# Add some spacing at the bottom
st.markdown("<br><br>", unsafe_allow_html=True)