-- Drop the vectors extension if it exists
DROP EXTENSION IF EXISTS vectors;

-- Create the vectors extension
CREATE EXTENSION vectors;

-- Create a table for storing text data and embeddings
CREATE TABLE text_data (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL,
    embedding VECTOR(768)  -- Adjust the dimension as needed (768 for the model used)
);
