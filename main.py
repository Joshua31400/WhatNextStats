import requests
from analyse_finance import generer_scatter_rentabilite
from analyse_genres import generer_box_plot_genres  # On importe la 2ème analyse

#clé API
API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxNTAzYmNiZTYwZTZlMWYwYTk2MzczYWEzZjFkMDQ3YiIsIm5iZiI6MTc3MjQ0NTExMy40OTQwMDAyLCJzdWIiOiI2OWE1NWRiOThlODAzN2ExNWJjMTdkYTIiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.W1Yi9LObmdHr90359Xkzj37iHavmsU8FeEMHADzzEEg"

HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}


def main():
    url = "https://api.themoviedb.org/3/movie/popular"
    params = {"language": "fr-FR", "page": 1}

    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        data = response.json().get('results', [])

        if data:
            print("\n--- Menu d'Analyse Cinématographique ---")
            print("1. Analyser la Rentabilité (Budget vs Recettes)")
            print("2. Analyser la Qualité par Genre (Box Plot)")
            print("3. Lancer les deux l'un après l'autre")

            choix = input("\nQuel graphique souhaitez-vous générer ? (1, 2 ou 3) : ")

            if choix == '1':
                generer_scatter_rentabilite(data, HEADERS)
            elif choix == '2':
                generer_box_plot_genres(data, HEADERS)
            elif choix == '3':
                print("Génération du premier graphique...")
                generer_scatter_rentabilite(data, HEADERS)
                print("Génération du deuxième graphique...")
                generer_box_plot_genres(data, HEADERS)
            else:
                print("Choix invalide.")
        else:
            print("Aucune donnée récupérée.")

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'appel API : {e}")


if __name__ == "__main__":
    main()