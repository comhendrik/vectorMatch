# Text Embedding and Search with PostgreSQL and Hugging Face in Docker

This project demonstrates a Python script that embeds text using a model from Hugging Face, stores the embeddings in PostgreSQL with the `pgvector` extension, and allows searching the database using regular text queries by comparing embeddings. After the data is retrieved an llm is used to generate a response with ollama. The Project is run with Docker Compose

## Features
- **Embeddings:** Use Hugging Face's transformers to embed input text.
- **PostgreSQL with pgvector:** Store embeddings in a PostgreSQL database using the `pgvector` extension to perform vector-based searches.
- **Search Functionality:** Retrieve database entries by comparing the input text's embedding to the stored embeddings.
- **Docker Support:** Run the whole application with Docker compose
- **Ollama:** Generate response based on local llm

## Prerequisites

Make sure you have the following installed:
- **Docker**

### Setup

Get the project directory
```
git clone https://github.com/comhendrik/vectorMatch.git
```
Start docker and go into the project directory and run the compose file
```
docker compose up
```
Wait for the script to be done, this can take a few minutes and then attach yourself to the vectorMatch container
```
docker attach vectormatch-vector-match-1
```
