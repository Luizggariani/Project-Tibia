CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE tibia_data (
    id SERIAL PRIMARY KEY,
    name TEXT,
    data JSONB,
    embedding VECTOR(384) -- adjust dimension to your embedding model
);
