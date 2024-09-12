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


def knn_query(embedding, k=3):
    """Find the k nearest neighbors for the given embedding."""
    query = sql.SQL(
        """
        SELECT id, text, embedding 
        FROM text_data
        ORDER BY embedding <-> %s 
        LIMIT %s
        """
    )
    cursor.execute(query, [embedding_to_pgvector(embedding), k])
    return cursor.fetchall()


# Embed a new sentence and perform a KNN search
new_text = "What is a three-pointer in basketball"

print(f"Query Text: {new_text}")
new_embedding = embed_text(new_text)

# Find the top 3 nearest neighbors
results = knn_query(new_embedding, k=3)

# Output the results
print("KNN Results:")
for result in results:
    print(f"ID: {result[0]}, Text: {result[1]}")

# Close the database connection
cursor.close()
connection.close()