# TMDb 2.3
# Send Feedback
# Fetch the names of the character played by Tom Cruise in the movies:
# Top Gun
# Mission: Impossible - Fallout
# Minority Report
# Edge of Tomorrow
# Output Format:
# Print the names of the characters played by Tom Cruise line separated, in the respective order given in question.


import numpy as np
import requests

response = requests.get("https://api.themoviedb.org/3/search/person?api_key=8fa1fff79901c54004d52192c68f8736&language=en-US&query=Tom%20Cruise")
# print(response.url)
data = response.json()
ids = data['results'][0]["id"]
# result
response2 = requests.get("https://api.themoviedb.org/3/person/500/movie_credits?api_key=8fa1fff79901c54004d52192c68f8736&language=en-US")
data2 = response2.json()
result = data2["cast"]
for i in result:
    if i["original_title"] == "Top Gun": 
        print(i["character"])
for i in result:
    if i["original_title"] == "Mission: Impossible - Fallout":
        print(i["character"])
for i in result:
    if i["original_title"] == "Minority Report":
        print(i["character"])
for i in result:
    if i["original_title"] == "Edge of Tomorrow":
        print(i["character"])
   
