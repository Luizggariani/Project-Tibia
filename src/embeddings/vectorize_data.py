import pandas as pd

class EmbeddingGenerator:
    def __init__(self, model):
        self.model = model

    def generate(self, text: str) -> list[float]:
        """Generate an embedding vector from a text."""
        return self.model.encode(text)

    def generate_from_dataframe(self, df: pd.DataFrame, column: str = "name") -> pd.DataFrame:
        """Generate embeddings for each row and return a new DataFrame with vectors."""
        df["embedding"] = df[column].apply(self.generate)
        return df
