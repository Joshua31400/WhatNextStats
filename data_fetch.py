import requests
import time
import json

class DataFetch:

    GENRE_MAP = {
        28: "Action", 12: "Adventure", 16: "Animation", 35: "Comedy",
        80: "Crime", 99: "Documentary", 18: "Drama", 10751: "Family",
        14: "Fantasy", 36: "History", 27: "Horror", 10402: "Music",
        9648: "Mystery", 10749: "Romance", 878: "Sci-Fi",
        53: "Thriller", 10752: "War", 37: "Western"
    }

    def __init__(self):
        self.API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxNTAzYmNiZTYwZTZlMWYwYTk2MzczYWEzZjFkMDQ3YiIsIm5iZiI6MTc3MjQ0NTExMy40OTQwMDAyLCJzdWIiOiI2OWE1NWRiOThlODAzN2ExNWJjMTdkYTIiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.W1Yi9LObmdHr90359Xkzj37iHavmsU8FeEMHADzzEEg"
        self.HEADERS = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.API_KEY}"
        }
        self.CACHE_FILE = "cache.json"

    def convert_genre_ids(self, movie):
        movie["genre_ids"] = [
            self.GENRE_MAP.get(gid, "Unknown") for gid in movie["genre_ids"]
        ]
        return movie

    def fetch_movie_details(self, movie_id):
        try:
            response = requests.get(
                f"https://api.themoviedb.org/3/movie/{movie_id}",
                headers=self.HEADERS,
                timeout=10
            )
            data = response.json()
            return {
                "budget_M":    data.get("budget",  0) / 1_000_000,
                "revenue_M":   data.get("revenue", 0) / 1_000_000,
                "runtime_min": data.get("runtime", None)
            }
        except Exception as e:
            print(f" ERROR on movie {movie_id}: {e}")
            return {"budget_M": None, "revenue_M": None, "runtime_min": None}

    def fetch_data(self, page_amount=1):
        print("Fetching data...")
        result = []

        for i in range(1, page_amount + 1):
            params = {"language": "en-US", "page": i}
            response = requests.get(
                "https://api.themoviedb.org/3/movie/popular",
                headers=self.HEADERS,
                params=params
            )
            data = response.json()
            movies = [self.convert_genre_ids(m) for m in data["results"]]
            result.extend(movies)
            print(f"Page {i}/{page_amount} → {len(result)} movies")

        print(f"\nFetching details (budget, revenue, runtime) for {len(result)} movies...")

        for i, movie in enumerate(result):
            details = self.fetch_movie_details(movie["id"])
            movie.update(details)
            print(f"\n Movie {i + 1}/{len(result)}")

        print("Data fetching completed.")
        return result

    def write_cache(self, data):
        with open(self.CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Cache written: {len(data)} movies → {self.CACHE_FILE}")

    def load_cache(self, movie_amount=None):
        with open(self.CACHE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        if movie_amount is not None:
            data = data[:movie_amount]

        print(f"Cache loaded: {len(data)} movies ← {self.CACHE_FILE}")
        return data

    def update_cache(self, page_amount=1):
        data = self.fetch_data(page_amount=page_amount)
        self.write_cache(data)