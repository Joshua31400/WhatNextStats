import pandas as pd
import matplotlib.pyplot as plt


class Seasonality:
    def __init__(self, df):
        self.df = df.copy()

    def calculate_stats(self):
        df = self.df.dropna(subset=["budget_M", "revenue_M"])
        df["profit_M"] = df["revenue_M"] - df["budget_M"]
        df["month"] = df["release_date"].dt.month

        monthly_profit = df.groupby("month")["profit_M"].mean()

        month_names = {1: "Jan", 2: "Fev", 3: "Mar", 4: "Abr", 5: "Mai", 6: "Jun",
                       7: "Jul", 8: "Ago", 9: "Set", 10: "Out", 11: "Nov", 12: "Dez"}

        monthly_profit.index = monthly_profit.index.map(month_names)

        colors = ["#FF6B6B" if v == monthly_profit.max() else "#4FC3F7" for v in monthly_profit.values]

        plt.figure(figsize=(12, 6))
        plt.bar(monthly_profit.index, monthly_profit.values, color=colors)
        plt.title("Average Profit by Release Month")
        plt.xlabel("Month")
        plt.ylabel("Average profit (M$)")
        plt.grid(axis="y", alpha=0.5)
        plt.tight_layout()
        plt.show()

        return monthly_profit