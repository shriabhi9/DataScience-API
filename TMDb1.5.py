# TMDb 1.5
# Send Feedback
# Fetch the top rated english movies in the US region using the TMDb API. From the result, print the first 10 movies which have original language as english. Also print their genres.
# Note: Do not use the search/movies API for finding genres.
# Output Format:
# movie_name_1 - genre_1, genre_2 ....
# and so on..

import requests
api_key = "your_api"
api_link = "https://api.themoviedb.org/3"
header = {'Accept': 'application/json'}
params = {'api_key':api_key, 'region':'US'}
response = requests.get(api_link + "/movie/top_rated", headers = header, params = params)
data = response.json()
results = data.get('results')
title_array = []
genre_id_array = []
for result in results:
    if result.get('original_language') == 'en':
        title_array.append(result.get('title'))
        genre_id_array.append(result.get('genre_ids'))
# To get the genre name corresponding to genre_id
response2 = requests.get(api_link + "/genre/movie/list", headers = header, params = params)
data2 = response2.json()
genres = data2.get('genres')
mapping = {}
for genre in genres:
    mapping[genre.get('id')] = genre.get('name')
for i in range(10):
    print(title_array[i], "-", end=" ")
    for id in genre_id_array[i]:
        print(mapping.get(id), end = ", ")
    print()
