import requests
from analyse_genres import generer_box_plot_genres

API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxNTAzYmNiZTYwZTZlMWYwYTk2MzczYWEzZjFkMDQ3YiIsIm5iZiI6MTc3MjQ0NTExMy40OTQwMDAyLCJzdWIiOiI2OWE1NWRiOThlODAzN2ExNWJjMTdkYTIiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.W1Yi9LObmdHr90359Xkzj37iHavmsU8FeEMHADzzEEg"

HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}


def main():
    url = "https://api.themoviedb.org/3/movie/popular"
    params = {
        "language": "fr-FR",
        "page": 1
    }

    try:
        # Requête à l'API
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()  # Vérifie s'il y a une erreur HTTP

        # Extraction des résultats (la liste des films)
        data = response.json().get('results', [])

        if data:
            print(f"Extraction de {len(data)} films réussie. Génération du graphique...")
            # Appel de la fonction importée de analyse_genres.py
            generer_box_plot_genres(data, HEADERS)
        else:
            print("Aucune donnée récupérée.")

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'appel API : {e}")


if __name__ == "__main__":
    main()