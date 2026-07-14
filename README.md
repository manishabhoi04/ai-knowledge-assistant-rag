\# 📚 RAG-Based PDF Question Answering Chatbot



\## Overview



This project is a Retrieval-Augmented Generation (RAG) chatbot that allows users to ask questions about PDF documents and receive context-aware answers with source citations.



The system extracts text from PDF files, converts document chunks into vector embeddings, stores them in a ChromaDB vector database, retrieves relevant chunks based on user queries, and generates answers using the Llama 3.2 Large Language Model through Ollama.



\---



\## Features



\* PDF text extraction

\* Document chunking

\* Embedding generation using Sentence Transformers

\* Semantic search using ChromaDB

\* Answer generation using Llama 3.2 (Ollama)

\* Source citation display

\* Interactive Streamlit user interface



\---



\## Tech Stack



\### Programming Language



\* Python



\### Libraries \& Frameworks



\* Streamlit

\* ChromaDB

\* Sentence Transformers

\* PyMuPDF

\* Requests

\* NumPy



\### Models



\* BAAI/bge-small-en-v1.5 (Embedding Model)

\* Llama 3.2 (Ollama)



\---



\## Project Workflow



PDF Document



↓



Text Extraction (PyMuPDF)



↓



Chunking



↓



Embedding Generation



↓



ChromaDB Vector Storage



↓



User Query



↓



Semantic Retrieval



↓



Llama 3.2 Generation



↓



Answer + Source Citations



\---



\## Project Structure



```text

RAG\_Learning/

│

├── data/

│   └── notes.pdf

│

├── chroma\_db/

│

├── app.py

├── rag\_engine.py

├── requirements.txt

│

├── 01\_pdf\_extraction.ipynb

└── 02\_metadata\_extraction.ipynb

```



\---



\## Installation



\### Clone Repository



```bash

git clone <your-repository-link>

cd RAG\_Learning

```



\### Install Dependencies



```bash

pip install -r requirements.txt

```



\### Install Ollama



Download and install Ollama:



https://ollama.com



Pull the Llama 3.2 model:



```bash

ollama pull llama3.2

```



\---



\## Running the Application



Start Ollama:



```bash

ollama serve

```



Run the Streamlit application:



```bash

streamlit run app.py

```



Open the browser:



```text

http://localhost:8501

```



\---



\## Example Query



Question:



```text

What is probability theory?

```



Answer:



```text

Probability theory is a branch of mathematics that deals with measuring the likelihood of events.

```



Sources:



```text

notes.pdf (Page 13)

notes.pdf (Page 11)

notes.pdf (Page 12)

```



\---



\## Learning Outcomes



Through this project, I learned:



\* Retrieval-Augmented Generation (RAG)

\* Embedding models

\* Vector databases

\* Semantic search

\* ChromaDB

\* Ollama

\* Streamlit application development

\* PDF document processing

\* End-to-end GenAI workflow



\---



\## Future Improvements



\* Multiple PDF support

\* File upload functionality

\* Conversation memory

\* Hybrid search

\* Improved UI/UX

\* Cloud deployment



\---



\## Author



Manisha Bhoi



AI/ML Engineer | Generative AI | Machine Learning | Python | RAG



