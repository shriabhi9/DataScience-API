# TMDb 3.2
# Send Feedback
# Fetch the name and air date of S06E05 of the TV Show 'The Big Bang Theory' from TMDb API.
# Output Format:
# episode_name - air_date

import requests
response = requests.get("https://api.themoviedb.org/3/search/tv?api_key=2b771a8d433185f787240fc50f7d077d&query=FRIENDS")
# print(response.url)
data = response.json()["results"]
for overview in data:
    if overview["original_name"] == "Friends":
        print(overview["overview"])
