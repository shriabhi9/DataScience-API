import requests
response = requests.get("https://api.themoviedb.org/3/trending/tv/week?api_key=2b771a8d433185f787240fc50f7d077d")
# print(response.url)
py_data = response.json()

ids = []
for i in py_data["results"]:
    ids.append(i["id"])
for i in ids[:5]:
    response2 = requests.get("https://api.themoviedb.org/3/tv/"+str(i)+"?api_key=2b771a8d433185f787240fc50f7d077d&language=en-US")
    data2 = response2.json()
    s = data2["tagline"]
    if len(s) == 0:
        print("Empty")
    else:
        print(s)
