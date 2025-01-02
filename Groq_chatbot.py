import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.chains import RetrievalQA

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Validate the API key
if not groq_api_key:
    st.error("GROQ_API_KEY is not set in the .env file.")
    raise ValueError("GROQ_API_KEY is required.")

# Initialize the Groq client
client = Groq(api_key=groq_api_key)

# Initialize embeddings and vector store
@st.cache_resource
def create_vector_store():
    # Load PDFs
    st.write("Loading documents from 'research_papers'...")
    loader = PyPDFDirectoryLoader("research_papers")
    documents = loader.load()
    
    # Split text into chunks
    st.write("Splitting documents into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_documents = text_splitter.split_documents(documents)
    
    # Generate embeddings
    st.write("Generating embeddings...")
    embeddings = OllamaEmbeddings()
    
    # Create and return a Chroma vector store
    st.write("Storing embeddings in vector store...")
    vector_store = Chroma.from_documents(
        documents=split_documents,
        embedding=embeddings,
        persist_directory=None  # In-memory vector store
    )
    return vector_store

# Streamlit UI
st.title("RAG Document Q&A with Groq")
st.write("Ask questions based on the content of your research papers!")

# Placeholder for creating vector store
if "vector_store" not in st.session_state:
    st.write("Initializing vector store...")
    st.session_state.vector_store = create_vector_store()
    st.success("Vector store is ready!")

# User input
user_query = st.text_input("Enter your question:")

# Placeholder for chatbot response
response_placeholder = st.empty()

if st.button("Ask"):
    if not user_query.strip():
        st.warning("Please enter a question before proceeding.")
    else:
        st.write("Fetching relevant context...")
        vector_store = st.session_state.vector_store
        
        # Retrieve relevant documents
        retriever = vector_store.as_retriever()
        relevant_docs = retriever.get_relevant_documents(user_query)
        context = " ".join([doc.page_content for doc in relevant_docs])
        
        if not context.strip():
            st.error("No relevant context found in the documents.")
        else:
            st.write("Context retrieved. Generating response...")
            
            # Stream the response using Groq
            try:
                completion = client.chat.completions.create(
                    model="llama2",
                    messages=[
                        {"role": "system", "content": "Use the following context to answer the user's question."},
                        {"role": "system", "content": f"Context: {context}"},
                        {"role": "user", "content": user_query},
                    ],
                    temperature=0.5,
                    max_tokens=1024,
                    top_p=0.65,
                    stream=True,
                    stop=None,
                )
                
                response_text = ""
                for chunk in completion:
                    chunk_content = chunk.choices[0].delta.content or ""
                    response_text += chunk_content
                    response_placeholder.text(response_text)
                
                st.success("Response generated!")
            except Exception as e:
                st.error(f"An error occurred while fetching the response: {str(e)}")
