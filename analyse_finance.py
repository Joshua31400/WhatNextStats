import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import time


def generer_scatter_rentabilite(movies_data, headers):
    finance_data = []
    print("Récupération des détails financiers (budget/recettes)...")

    for movie in movies_data[:20]:  # On limite aux 20 premiers pour l'exemple
        movie_id = movie['id']
        url = f"https://api.themoviedb.org/3/movie/{movie_id}"

        res = requests.get(url, headers=headers).json()

        # On ne garde que les films qui ont des données renseignées
        if res.get('budget', 0) > 0 and res.get('revenue', 0) > 0:
            finance_data.append({
                'Titre': res.get('title'),
                'Budget': res.get('budget'),
                'Recettes': res.get('revenue')
            })
        time.sleep(0.1)  # Petite pause pour respecter l'API

    df = pd.DataFrame(finance_data)

    # Création du Scatter Plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Budget', y='Recettes', size='Recettes', sizes=(20, 200))

    # Ligne de rentabilité (x=y)
    max_val = max(df['Budget'].max(), df['Recettes'].max())
    plt.plot([0, max_val], [0, max_val], 'r--', label='Seuil de rentabilité')

    plt.title("Rentabilité des films : Budget vs Recettes")
    plt.legend()
    plt.show()