# TMDb 3.1
# Send Feedback
# Fetch the overview of the TV Show "FRIENDS" using TMDb API.
# Output Format:
# Print the Overview.

import requests
response = requests.get("https://api.themoviedb.org/3/search/tv?api_key=2b771a8d433185f787240fc50f7d077d&query=FRIENDS")
# print(response.url)
data = response.json()["results"]
for overview in data:
    if overview["original_name"] == "Friends":
        print(overview["overview"])
