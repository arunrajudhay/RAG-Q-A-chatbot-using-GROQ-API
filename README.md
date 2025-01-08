# RAG Document Q&A with Groq
Welcome to the RAG Document Q&A with Groq application! This application allows you to interact with pdf documents, asking questions, and receiving answers based on the content of those documents using a Retrieval-Augmented Generation (RAG) approach with the power of Groq's API and LangChain.

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
* PyPDF2

To install all the necessary dependencies, simply run :  
pip install -r requirements.txt

## Setup Instructions
1. Clone the Repository
2. Set up Environment Variables
3. Upload pdf documents
4. Run the Application

## How It Works
1. Document Loading: The PDF documents in the research_papers directory are loaded using PyPDFDirectoryLoader and split into chunks using RecursiveCharacterTextSplitter for easier processing.
2. Embeddings: The loaded documents are embedded using OllamaEmbeddings, which allows for efficient comparison and retrieval of relevant document chunks based on user queries.
3. Vector Storage: The embeddings are stored in an in-memory Chroma vector store, allowing fast retrieval of relevant documents.
4. Query Answering: When a user submits a query, the application retrieves the most relevant document chunks, sends them along with the query to Groq's LLM for response generation, and streams the response in real-time.

## Example Usage
1. Open the app, and you'll be prompted to enter a question.
2. After entering a question, click on the "Ask" button.
3. The app will fetch relevant document context and provide an answer in real-time.

## Sample Output
* User Query: "What are the latest trends in AI research?"
* Generated Answer: Based on the context of the uploaded documents, the model will respond with an accurate answer.

## Contributing
Contributions to this chatbot project are highly encouraged! If you find any bugs, have feature requests, or would like to suggest enhancements, please feel free to open an issue or submit a pull request. Your input will help improve the chatbot's functionality and user experience. Thank you for your interest and support!
To Do:
Improve UI/UX with better design.
Add support for more document formats (e.g., Word, PPT).
Optimize query-answering speed with larger datasets.

## Contact:

Email : [ruarunraj2013@gmail.com](mailto:ruarunraj2013@gmail.com)

Linkedin : https://www.linkedin.com/in/arunraj-r-u-27722a146

Thanks for showing interest in this repository. !


