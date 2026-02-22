import requests
def get_weather(city):
    api_key = 'your_api_key_here'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        return {
            'temperature': main['temp'],
            'humidity': main['humidity'],
            'description': weather['description']
        }
    else:
        return None
def display_weather(city):
    weather = get_weather(city)
    if weather:
        print(f"Weather in {city}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Description: {weather['description']}")
    else:
        print("Could not retrieve weather data.")

if __name__ == "__main__":
    city = input("Enter the city name: ")
    display_weather(city)
# Note: Replace
# 'your_api
# key_here' with your actual OpenWeatherMap API key.