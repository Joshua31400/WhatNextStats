import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def generer_box_plot_genres(movies_data):
    results = []
    for movie in movies_data:
        for genre in movie.get('genre_ids', []):
            results.append({
                'Titre': movie.get('title'),
                'Genre': genre,
                'Note': movie.get('vote_average')
            })

    df = pd.DataFrame(results)
    df = df.dropna(subset=['Genre', 'Note'])

    plt.figure(figsize=(12, 8))
    sns.boxplot(data=df, x='Genre', y='Note', color="#4FC3F7")
    plt.xticks(rotation=45)
    plt.title("Dispersion des notes par genre (Films Populaires)")
    plt.tight_layout()
    plt.show()