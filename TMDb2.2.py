# TMDb 2.2
# Send Feedback
# Fetch the Instagram and Twitter handle of Indian Actress "Alia Bhatt" from the TMDb API.
# Output Format
# Print the Instagram and Twitter IDs space separated.
# instagram_id twitter_id

import requests
response = requests.get("https://api.themoviedb.org/3/search/person?api_key=8fa1fff79901c54004d52192c68f8736&language=en-US&query=Alia%20Bhatt")
# print(response.url)
data = response.json()
result = data['results'][0]["id"]

response2 = requests.get("https://api.themoviedb.org/3/person/1108120/external_ids?api_key=8fa1fff79901c54004d52192c68f8736&language=en-US")
data2 = response2.json()
print(data2["instagram_id"],end=" ")
print(data2["twitter_id"])
