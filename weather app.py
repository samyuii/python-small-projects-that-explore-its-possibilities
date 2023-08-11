import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url)
    weather_data = response.json()
    return weather_data

def display_weather(weather_data):
    if weather_data["cod"] == 200:
        weather_description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"] - 273.15  # Convert to Celsius
        humidity = weather_data["main"]["humidity"]
        print(f"Weather: {weather_description}")
        print(f"Temperature: {temperature:.2f}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("City not found or an error occurred.")


while True:
    print("Welcome to the Weather Information App!")
    city = input("Enter the name of a city (or 'exit' to quit): ")

    if city.lower() == "exit":
        print("Thanks for using the Weather Information App. Have a great day!")
        break
    else:
        weather_data = get_weather(city)
        display_weather(weather_data)
        print("\n")
