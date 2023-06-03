# TMDb 1.3
# Send Feedback
# Find the vote count and vote average of the movie "3 Idiots" using the TMDb API
# Output format: Vote Count , Vote Average

import requests
import json

response = requests.get("https://api.themoviedb.org/3/movie/20453?api_key=8fa1fff79901c54004d52192c68f8736")
# print(response.url)
py_data = response.json()
print(py_data['vote_count'],py_data['vote_average'])
