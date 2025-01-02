"""Objective: The aim of this assignment is to refactor an existing Python script for a weather forecast application into a more structured, 
object-oriented, and modular format. The focus will be on identifying parts of the script that can be encapsulated into classes 
and organizing these classes into appropriate modules to enhance code readability, maintainability, and scalability.

Task 1: Identifying and Creating Classes Analyze the provided script and identify distinct functionalities that can be encapsulated into classes. 
Create classes that represent different aspects of the weather forecast application, such as fetching data, parsing data, and user interaction.

Problem Statement: The existing script for the weather forecast application is written in a procedural style and lacks organization. """

class WeatherDataFetcher:
    def __init__(self, weather_data):
        self.weather_data = weather_data

    def fetch(self, city):
        # Debugging print statement to check the input city and weather data
        print(f"Fetching weather data for {city}...")
        return self.weather_data.get(city.title(), {})  # Ensure the city name is properly capitalized

class DataParser:
    def parse(self, data): # Going through each value in our dictionary one by one
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

class UserInterface:
    def __init__(self, data_fetcher, parser):
        self.data_fetcher = data_fetcher
        self.parser = parser

    def display_weather(self, city):
        # Get the weather data 
        data = self.data_fetcher.fetch(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = self.parser.parse(data) 
            print(weather_report)

    def get_detailed_forecast(self, city):
        # Get the detailed weather forecast
        data = self.data_fetcher.fetch(city)
        return self.parser.parse(data)

    def get_user_input(self):
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        return city.strip()  # Remove any whitespace

    def ask_for_details(self):
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        return detailed == 'yes'


def main():
    # Predefined weather data
    weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
    }

#    Examples using the classes
    data_fetcher = WeatherDataFetcher(weather_data)
    parser = DataParser()
    user_interface = UserInterface(data_fetcher, parser)

    while True:
        city = user_interface.get_user_input()
        if city.lower() == 'exit':
            break
        if user_interface.ask_for_details():
            forecast = user_interface.get_detailed_forecast(city)
        else:
            forecast = user_interface.display_weather(city)
        print(forecast)

if __name__ == "__main__":
    main()
