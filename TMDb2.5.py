# TMDb 2.5
# Send Feedback
# Using the result obtained in previous question, find out if James McAvoy was credited for his role in movie Deadpool 2. Print Yes or No.

import requests
response = requests.get("https://api.themoviedb.org/3/search/person?api_key=2b771a8d433185f787240fc50f7d077d&language=en-US&query=James%20McAvoy")
# print(response.url)
data = response.json()
ids = data['results'][0]["id"]
# ids
response2 = requests.get("https://api.themoviedb.org/3/person/" + str(ids) + "/movie_credits?api_key=2b771a8d433185f787240fc50f7d077d")
data2 = response2.json()
# print(response2.url)
cast = data2["cast"]
for i in cast:
    if i["original_title"] == "Deadpool 2":
        print("No")
