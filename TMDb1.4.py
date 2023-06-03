# TMDb 1.4
# Send Feedback
# Fetch the names of top 5 similar movies to 'Inception' from the TMDb API.
# Note
# While fetching the movie id, use the "original_title" field not the "title". Because the "title" field may contain duplicate values.
# Output Format:
# Print the name of the movies in a new line.
# movie_name_1
# movie_name_2
# and so on

import requests
api_key = "Your_api"
api_link = "https://api.themoviedb.org/3" 

params = {'query':"Inception", 'api_key':api_key} 

h = header = {'Accept': 'application/json'} 
response = requests.get(api_link + "/search/movie", headers = header, params=params)
data = response.json() 
results = data.get('results') 
for result in results: 
    if result.get('original_title') == 'Inception':
        id = result.get('id') 
        

params2={'api_key':api_key}
call=requests.get('https://api.themoviedb.org/3/movie/27205/similar',params=params2,headers=h)
#call.status_code
li = call.json()['results']
for ele in li[0:5]:
    print(ele['title'])
    
