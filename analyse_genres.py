import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def generer_box_plot_genres(movies_data, headers):
    # 1. Récupérer la correspondance ID -> Nom du genre
    import requests
    url_genres = "https://api.themoviedb.org/3/genre/movie/list?language=fr"
    genres_list = requests.get(url_genres, headers=headers).json()['genres']
    genre_map = {g['id']: g['name'] for g in genres_list}

    # 2. Préparer les données pour Pandas
    results = []
    for movie in movies_data:
        for genre_id in movie.get('genre_ids', []):
            results.append({
                'Titre': movie.get('title'),
                'Genre': genre_map.get(genre_id),
                'Note': movie.get('vote_average')
            })

    df = pd.DataFrame(results)

    # 3. Création du Box Plot
    plt.figure(figsize=(12, 8))
    sns.boxplot(data=df, x='Genre', y='Note', palette="Set3")
    plt.xticks(rotation=45)
    plt.title("Dispersion des notes par genre (Films Populaires)")
    plt.tight_layout()
    plt.show()