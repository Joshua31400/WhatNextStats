import requests

API_KEY  = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxNTAzYmNiZTYwZTZlMWYwYTk2MzczYWEzZjFkMDQ3YiIsIm5iZiI6MTc3MjQ0NTExMy40OTQwMDAyLCJzdWIiOiI2OWE1NWRiOThlODAzN2ExNWJjMTdkYTIiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.W1Yi9LObmdHr90359Xkzj37iHavmsU8FeEMHADzzEEg"

HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

params = {"language": "en-US", "page": 1}

if __name__ == "__main__":
    response = requests.get("https://api.themoviedb.org/3/movie/popular", headers=HEADERS, params=params)
    print(response.text)