import requests
## Write your code here
import requests
# apiKey = 'ffafe1f2b141d9a9fcae15771fe46db1'
## Write your code here
res = requests.get(f'https://api.themoviedb.org/3//tv/airing_today?api_key=c259e364e3cd2e5b4013d7342c7f33fa')
data=res.json()
total=data['total_pages']
for i in range(1,total+1):
  res = requests.get(f'https://api.themoviedb.org/3//tv/airing_today?api_key=c259e364e3cd2e5b4013d7342c7f33fa',params={'page':i}) 
  data=res.json()
  for j  in data['results']:
    if j['original_language']=='en':
      print(j['name'])
     
