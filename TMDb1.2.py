# TMDb 1.2
# Send Feedback
# Fetch the company id company 'Marvel Studios' using TMDb. Print the id.

import requests
import json

response = requests.get("https://api.themoviedb.org/3/company/420?api_key=YOUR")
# print(response.url)
py_data = response.json()
print(py_data['id'])
