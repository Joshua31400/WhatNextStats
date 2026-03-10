import pandas as pd
import matplotlib.pyplot as plt

class HeatmapGenerator:
    def __init__(self, df: pd.DataFrame, movie_amount: int = 200):
        self.df = df.copy()
        self.df = self.df.head(movie_amount)

    def _explode_genres(self) -> pd.DataFrame:
        df = self.df.copy()

        # explode() transforms each element of a list-like structure to a row
        df = df.explode("genres")

        df = df.dropna(subset=["genres"])

        return df

    def _add_year(self, df: pd.DataFrame) -> pd.DataFrame:
        df["year"] = df["release_date"].dt.year
        return df

    def _build_pivot(self, df: pd.DataFrame) -> pd.DataFrame:
        pivot = df.pivot_table(
            index="genres",
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

        plt.tight_layout()
        plt.show()

    def generate(self):
        df_exploded = self._explode_genres()
        df_enriched = self._add_year(df_exploded)
        pivot = self._build_pivot(df_enriched)

        self._draw_heatmap(pivot)
