import requests
import argparse

def get_weather(location):
    api_key = 'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}'  # Replace with your actual API key
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        weather_data = response.json()

        # Display weather information in the terminal
        print(f"Weather in {weather_data['name']}:")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

def main():
    parser = argparse.ArgumentParser(description='Get weather information')
    parser.add_argument('location', type=str, help='Location name or zip code')
    args = parser.parse_args()

    get_weather(args.location)

if __name__ == "__main__":
    main()
