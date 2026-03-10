import pandas as pd
import matplotlib.pyplot as plt

class EvolutionTemporelle:
    def __init__(self, df):
        self.df = df.copy()

        if 'year' not in self.df.columns and 'release_date' in self.df.columns:
            self.df['year'] = pd.to_datetime(self.df['release_date']).dt.year

    def calculate_stats(self):
        df_finance = self.df.dropna(subset=["budget_M", "revenue_M"])
        df_finance = df_finance[(df_finance["year"] >= 1990) & (df_finance["year"] <= 2024)]

        evolution = df_finance.groupby("year")[["budget_M", "revenue_M"]].mean()

        plt.figure(figsize=(12, 6))
        plt.plot(evolution.index, evolution["budget_M"], label="Budget Moyen (M$)", color="#FF6B6B", linewidth=2, marker="o")
        plt.plot(evolution.index, evolution["revenue_M"], label="Recette Moyenne (M$)", color="#4FC3F7", linewidth=2, marker="o")

        plt.title("Évolution temporelle : Recettes et budgets moyens (1990 - 2024)")
        plt.xlabel("Année")
        plt.ylabel("Montant (M$)")
        plt.legend()
        plt.grid(True, alpha=0.5)
        plt.tight_layout()
        plt.show()

        return evolution