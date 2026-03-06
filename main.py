import requests
from data_clean import DataCleaner

API_KEY  = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxNTAzYmNiZTYwZTZlMWYwYTk2MzczYWEzZjFkMDQ3YiIsIm5iZiI6MTc3MjQ0NTExMy40OTQwMDAyLCJzdWIiOiI2OWE1NWRiOThlODAzN2ExNWJjMTdkYTIiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.W1Yi9LObmdHr90359Xkzj37iHavmsU8FeEMHADzzEEg"

HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

params = {"language": "en-US", "page": 1}

if __name__ == "__main__":
    response = requests.get(
        "https://api.themoviedb.org/3/movie/popular",
        headers=HEADERS,
        params={"language": "en-US", "page": 1}
    )

    print(response.text)

    movies = response.json().get("results", [])
    cleaner = DataCleaner(movies)
    df_clean = cleaner.run_pipeline()

    print(f" Cleaned movies: {len(df_clean)}")
    print(f"Memory weight: {df_clean.memory_usage(deep=True).sum() / 1024:.2f} KB")
    print(df_clean.head().to_string())