import requests
class DataFetch:


    def __init__(self):
        self.API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxNTAzYmNiZTYwZTZlMWYwYTk2MzczYWEzZjFkMDQ3YiIsIm5iZiI6MTc3MjQ0NTExMy40OTQwMDAyLCJzdWIiOiI2OWE1NWRiOThlODAzN2ExNWJjMTdkYTIiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.W1Yi9LObmdHr90359Xkzj37iHavmsU8FeEMHADzzEEg"

        self.HEADERS = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.API_KEY}"
        }

    def fetch_data(self, page_amount=100):
        print("Fetching data...")
        result = []
        for i in range(1, page_amount):
            params = {"language": "en-US", "page": i}
            response = requests.get("https://api.themoviedb.org/3/movie/popular", headers=self.HEADERS, params=params)
            data = response.json()
            result.extend(data["results"])
            print("Page: ", i, " - movies fetched: ", len(result))
        print("Data fetching completed.")
        return result
