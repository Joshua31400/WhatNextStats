import pandas as pd
import matplotlib.pyplot as plt


class DurationPerYear:
    def __init__(self, df):
        self.df = df.copy()

    def calculate_stats(self):
        df = self.df.dropna(subset=["runtime_min"])
        df = df[df["runtime_min"] > 0]

        df["year"] = df["release_date"].dt.year
        duration_by_year = df.groupby("year")["runtime_min"].mean()

        plt.figure(figsize=(12, 6))
        plt.plot(duration_by_year.index, duration_by_year.values, color="#4FC3F7", lw=2.5)
        plt.fill_between(duration_by_year.index, duration_by_year.values, alpha=0.2, color="#4FC3F7")
        plt.axhline(duration_by_year.mean(), color="#FF6B6B", linestyle="--", lw=1.5,
                    label=f"Overall Average: {duration_by_year.mean():.0f} min")
        plt.title("Average Movie Duration per Year")
        plt.xlabel("Year")
        plt.ylabel("Average Duration (min)")
        plt.legend()
        plt.grid(axis="y", alpha=0.5)
        plt.tight_layout()
        plt.show()

        return duration_by_year