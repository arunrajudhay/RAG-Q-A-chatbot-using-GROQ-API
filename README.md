# RAG Document Q&A with Groq
Welcome to the RAG Document Q&A with Groq application! This application allows you to interact with research papers, asking questions, and receiving answers based on the content of those documents using a Retrieval-Augmented Generation (RAG) approach with the power of Groq's API and LangChain.

## Features
* Document Loading & Processing: Load PDF documents from a directory, split them into manageable chunks, and prepare them for query answering.
* Embedding & Vector Storage: Use Ollama Embeddings to convert documents into vectors, stored in an in-memory Chroma vector store.
* Real-Time Q&A: Stream user queries to Groq's powerful LLM to generate answers based on the relevant context pulled from research papers.

## Requirements
To run this application locally, you need to have the following libraries:

* streamlit
* python-dotenv
* groq
* langchain-community
* langchain
* requests
* PyPDF2
* numpy

To install all the necessary dependencies, simply run :  
pip install -r requirements.txt

## Setup Instructions
1. Clone the Repository
2. Set up Environment Variables
3. Upload Research Papers
4. Run the Application

## How It Works
1. Document Loading: The PDF documents in the research_papers directory are loaded using PyPDFDirectoryLoader and split into chunks using RecursiveCharacterTextSplitter for easier processing.
2. Embeddings: The loaded documents are embedded using OllamaEmbeddings, which allows for efficient comparison and retrieval of relevant document chunks based on user queries.
3. Vector Storage: The embeddings are stored in an in-memory Chroma vector store, allowing fast retrieval of relevant documents.
4. Query Answering: When a user submits a query, the application retrieves the most relevant document chunks, sends them along with the query to Groq's LLM for response generation, and streams the response in real-time.


