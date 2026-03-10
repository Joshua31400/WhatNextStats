import matplotlib.pyplot as plt

class GenresProduits:
    def __init__(self, df):
        self.df = df.copy()

    def calculate_stats(self):
        df_exploded = self.df.explode("genres")
        df_exploded = df_exploded.dropna(subset=["genres"])
        df_exploded = df_exploded[df_exploded["genres"] != "Unknown"]

        genres_count = df_exploded["genres"].value_counts().head(15).sort_values()

        colors = ["#FF6B6B" if v == genres_count.max() else "#4FC3F7" for v in genres_count.values]

        plt.figure(figsize=(12, 6))
        plt.barh(genres_count.index, genres_count.values, color=colors)
        plt.title("Genres dominants sur le marché")
        plt.xlabel("Nombre de films")
        plt.ylabel("Genre")
        plt.grid(axis="x", alpha=0.5)
        plt.tight_layout()
        plt.show()

        return genres_count