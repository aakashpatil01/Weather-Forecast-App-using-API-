import requests

API_KEY = "846cf96e6cbfbde0094820f8339ea08d"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """Fetch and display current weather for a given city."""
    response = requests.get(BASE_URL, params={
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    })

    if response.status_code != 200:
        print("Error: City not found or invalid API key.")
        return

    data = response.json()

    city_name = data["name"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"].capitalize()

    print(f"\nWeather Report — {city_name}")
    print(f"  Temperature : {temperature}°C")
    print(f"  Humidity    : {humidity}%")
    print(f"  Condition   : {condition}")


if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
