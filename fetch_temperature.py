import requests

def fetch_temperature(lat, lon):
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&current=temperature_2m"
    )

    data = response.json()
    return data["current"]["temperature_2m"]