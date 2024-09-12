import psycopg2
from psycopg2 import sql
from transformers import AutoTokenizer, AutoModel
import torch

# Load Hugging Face model and tokenizer for embeddings
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"  # A small embedding model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModel.from_pretrained(MODEL_NAME)


def embed_text(text):
    """Generate embeddings for the given text using Hugging Face transformer model."""
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    # Typically we take the mean of token embeddings for the sentence embedding
    embedding = outputs.last_hidden_state.mean(dim=1).squeeze().tolist()  # Convert to list of floats
    return embedding

def embedding_to_pgvector(embedding):
    """Convert the embedding list to a format compatible with PostgreSQL pgvector."""
    embedding_str = "[" + ", ".join(f"{x:.6f}" for x in embedding) + "]"

    return embedding_str


# Connect to the PostgreSQL database
connection = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="mysecretpassword"
)
cursor = connection.cursor()

# Sample data
texts = [
    "This is sample text, to test embedding"
]

# Step 1: Insert sample text and embeddings into the database
i=6
for data in texts:
    result = embed_text(data)
    # Store the text and its embedding vector into PostgreSQL
    insert_query = sql.SQL(
        "INSERT INTO text_data (text, embedding) VALUES (%s, %s)"
    )
    cursor.execute(insert_query, [data, embedding_to_pgvector(result)])
    connection.commit()
    i += 1

connection.close()
# Step 2: Perform a KNN query on the embeddings

