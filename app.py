import requests

# URL de l'API avec paramètre de langue pour obtenir des blagues en français
url = "https://v2.jokeapi.dev/joke/Any?lang=fr"

response = requests.get(url)
data = response.json()

# Afficher la blague
if data['type'] == 'single':
    print(data['joke'])
else:
    print(f"{data['setup']} - {data['delivery']}")
