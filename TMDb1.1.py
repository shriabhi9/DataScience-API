# TMDb 1.1
import requests
import json

response = requests.get("https://api.themoviedb.org/3/movie/534780?api_key=YOUR_API")
# print(response.url)
py_data = response.json()
print(py_data['id'])
