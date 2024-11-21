import requests


url = "https://v2.jokeapi.dev/joke/Any?lang=fr"

response = requests.get(url)
data = response.json()


if data['type'] == 'single':
    print(data['joke'])
else:
    print(f"{data['setup']} - {data['delivery']}")
