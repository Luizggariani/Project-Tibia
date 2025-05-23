CREATE EXTENSION IF NOT EXISTS vector;

ALTER EXTENSION vector UPDATE;

CREATE TABLE tibia_data (
    id SERIAL PRIMARY KEY,
    name TEXT,
    data JSONB,
    embedding VECTOR(384) -- adjust dimension to your embedding model
);