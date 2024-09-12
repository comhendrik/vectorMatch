# Text Embedding and Search with PostgreSQL and Hugging Face in Docker

This project demonstrates a Python script that embeds text using a model from Hugging Face, stores the embeddings in PostgreSQL with the `pgvector` extension, and allows searching the database using regular text queries by comparing embeddings.

## Features
- **Embeddings:** Use Hugging Face's transformers to embed input text.
- **PostgreSQL with pgvector:** Store embeddings in a PostgreSQL database using the `pgvector` extension to perform vector-based searches.
- **Search Functionality:** Retrieve database entries by comparing the input text's embedding to the stored embeddings.
- **Docker Support:** Run PostgreSQL and the pgvector extension within Docker for easy setup and deployment.

## Prerequisites

Make sure you have the following installed:
- **Docker** (to run PostgreSQL with pgvector)
- **Python 3.x** (for the Python script)
- **pip** (Python package manager)

### Python Dependencies
The Python script requires the following libraries, which can be installed via the `requirements.txt` file:
- `psycopg2`: For connecting to PostgreSQL.
- `transformers`: Hugging Face library to handle text embeddings.
- `torch`: Backend library for running the transformer model.

### Setup

Run Postgres DB with pgvecto.rs in a docker container
```
docker run \
--name pgvecto-rs-demo \
-e POSTGRES_PASSWORD=mysecretpassword \
-p 5432:5432 \
-d tensorchord/pgvecto-rs:pg16-v0.2.0
```
Then you can connect to the database using the psql command line tool. The default username is postgres, and the default password is mysecretpassword.
```
psql postgresql://postgres:mysecretpassword@localhost:5432/postgres
```
Run the following SQL to ensure the extension is enabled.
```
DROP EXTENSION IF EXISTS vectors;
CREATE EXTENSION vectors;
```
Create Table text_data
```
CREATE TABLE text_data (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL,
    embedding VECTOR(768)  -- Adjust the dimension (768) as needed, but for the used model its 768
);
```
Create a venv in your projects repository and install the packages
```
python -m venv myenv           # Create a virtual environment
source myenv/bin/activate      # Activate the environment (macOS/Linux)
# myenv\Scripts\activate        # Activate the environment (Windows)
pip install -r requirements.txt # Install dependencies
```
Run python files
Embeed and save text
```
python (or python3) vectorize.py
```
Search For Querys
```
python (or python3) search.py
```