import pandas as pd
import matplotlib.pyplot as plt

GENRE_MAP = {
    28: "Action",
    12: "Adventure",
    16: "Animation",
    35: "Comedy",
    80: "Crime",
    99: "Documentary",
    18: "Drama",
    10751: "Family",
    14: "Fantasy",
    36: "History",
    27: "Horror",
    10402: "Music",
    9648: "Mystery",
    10749: "Romance",
    878: "Sci-Fi",
    10770: "TV Movie",
    53: "Thriller",
    10752: "War",
    37: "Western",
}


class HeatmapGenerator:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def _explode_genres(self) -> pd.DataFrame:
        df = self.df.copy()

        # explode() transforms each element of a list-like structure to a row
        df = df.explode("genre_ids")

        df["genre_ids"] = pd.to_numeric(df["genre_ids"], errors="coerce")

        df = df.dropna(subset=["genre_ids"])
        df["genre_ids"] = df["genre_ids"].astype(int)

        return df

    def _add_year_and_genre_name(self, df: pd.DataFrame) -> pd.DataFrame:
        # .dt.year extracts the year from a datetime column
        df["year"] = df["release_date"].dt.year

        df["genre_name"] = df["genre_ids"].map(GENRE_MAP).fillna("Unknown")

        return df

    def _build_pivot(self, df: pd.DataFrame) -> pd.DataFrame:
        pivot = df.pivot_table(
            index="genre_name",
            columns="year",
            values="vote_average",
            aggfunc="mean"
        )

        pivot = pivot.round(2)

        return pivot

    def _draw_heatmap(self, pivot: pd.DataFrame):
        n_genres = len(pivot.index)
        n_years = len(pivot.columns)

        # figsize adapts the height and width of the figure based on the number of genres and years
        fig, ax = plt.subplots(figsize=(max(6, n_years * 1.2), max(4, n_genres * 0.6)))

        cmap = plt.cm.YlOrRd

        im = ax.imshow(pivot.values, cmap=cmap, aspect="auto")

        # Define positions for labels
        ax.set_xticks(range(n_years))
        ax.set_xticklabels([str(int(y)) for y in pivot.columns], rotation=45, ha="right")

        ax.set_yticks(range(n_genres))
        ax.set_yticklabels(pivot.index)

        # Display values in cells
        for row_idx in range(n_genres):
            for col_idx in range(n_years):
                value = pivot.values[row_idx, col_idx]

                # Check if the value is NaN
                if pd.isna(value):
                    continue

                # Use black text for light backgrounds, white text for dark backgrounds
                norm_value = (value - pivot.min().min()) / (pivot.max().max() - pivot.min().min())
                text_color = "white" if norm_value > 0.6 else "black"

                ax.text(
                    col_idx, row_idx,
                    f"{value:.2f}",
                    ha="center",
                    va="center",
                    fontsize=8,
                    color=text_color
                )

        cbar = plt.colorbar(im, ax=ax)
        cbar.set_label("Average Rating", rotation=270, labelpad=15)

        ax.set_title("Evolution of Average Rating by Genre Over Time", pad=15)
        ax.set_xlabel("Release Year")
        ax.set_ylabel("Genre")

        # Adjust layout automatically
        plt.tight_layout()
        plt.show()

    def generate(self):
        df_exploded = self._explode_genres()
        df_enriched = self._add_year_and_genre_name(df_exploded)
        pivot = self._build_pivot(df_enriched)

        print(f"Detected genres: {list(pivot.index)}")
        print(f"Detected years: {list(pivot.columns)}")
        print("\nPivot table (average rating by genre × year):")
        print(pivot.to_string())

        self._draw_heatmap(pivot)
