import pandas as pd
import matplotlib.pyplot as plt


class RoiPerGenre:
    def __init__(self, df):
        self.df = df.copy()

    def calculate_stats(self):
        df = self.df.dropna(subset=["budget_M", "revenue_M"])
        df = df[df["budget_M"] > 0]
        df["roi"] = (df["revenue_M"] - df["budget_M"]) / df["budget_M"] * 100

        df_exploded = df.explode("genres")
        roi_by_genre = df_exploded.groupby("genres")["roi"].mean().sort_values()

        colors = ["#FF6B6B" if v == roi_by_genre.max() else "#4FC3F7" for v in roi_by_genre.values]

        plt.figure(figsize=(12, 6))
        plt.barh(roi_by_genre.index, roi_by_genre.values, color=colors)
        plt.title("Average ROI by Genre")
        plt.xlabel("Average ROI (%)")
        plt.ylabel("Genre")
        plt.grid(axis="x", alpha=0.5)
        plt.tight_layout()
        plt.show()

        return roi_by_genre