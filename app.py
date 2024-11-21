import requests


def fetch_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    try:
        response = requests.get(url)
        response.raise_for_status()
        joke_data = response.json()

        if joke_data["type"] == "single":
            print(f"Joke: {joke_data['joke']}")
        else:
            print(f"Setup: {joke_data['setup']}")
            print(f"Delivery: {joke_data['delivery']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching joke: {e}")


if __name__ == "__main__":
    fetch_joke()