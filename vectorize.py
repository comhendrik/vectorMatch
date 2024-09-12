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
    # Football-related sentences
    "The football game ended in a thrilling 3-2 victory.",
    "He scored a hat-trick in the last football match.",
    "The quarterback threw a perfect pass for the touchdown.",
    "Football fans filled the stadium with excitement.",
    "She loves playing football with her friends every weekend.",
    "The defender blocked the shot at the last moment.",
    "His football skills have improved drastically over the summer.",
    "The World Cup is one of the biggest football tournaments in the world.",
    "The team celebrated their football championship with a parade.",
    "Football requires both physical strength and tactical awareness.",

    # Basketball-related sentences
    "The basketball game went into overtime after a tie.",
    "He made a three-pointer to win the basketball game.",
    "The point guard dribbled past the defender and scored.",
    "Basketball players need great agility and hand-eye coordination.",
    "She enjoys playing basketball at the local court every afternoon.",
    "The slam dunk brought the crowd to their feet.",
    "His free-throw accuracy is improving every practice.",
    "Basketball is a fast-paced game that requires quick reflexes.",
    "They cheered as their team advanced to the basketball finals.",
    "The coach emphasized teamwork and passing during basketball practice.",

    # Golf-related sentences
    "He made an impressive hole-in-one on the 7th hole.",
    "Golf requires a combination of precision and patience.",
    "The golf course was in pristine condition for the tournament.",
    "She enjoys golfing on weekends with her family.",
    "His swing has improved significantly after taking golf lessons.",
    "The golf ball landed just inches from the hole.",
    "The golfer calmly lined up his putt and sank it.",
    "Golf can be a relaxing yet challenging sport.",
    "The golf club selection is crucial for each shot.",
    "The final round of the golf tournament was extremely competitive."
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

