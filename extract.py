import requests
import pandas as pd
import datetime
import os

# Cấu hình API
API_KEY = 'insert_your_openweathermap_api_key_here'  # Remember to replace this with your actual OpenWeatherMap API key
CITIES = ['Hanoi', 'Ho Chi Minh', 'Da Nang', 'Tokyo', 'London'] 
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def fetch_weather_data(city):
    params = {
        'q': city, 
        'appid': API_KEY, 
        'units': 'metric' #use metric units for temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for {city}: {response.status_code}")
        return None

def process_data(data):
    """Filter and structure the raw data into a dictionary format."""
    return {
        'city': data['name'],
        'country': data['sys']['country'],
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        'weather_condition': data['weather'][0]['main'],
        'extraction_date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def main():
    weather_records = []
    for city in CITIES:
        print(f"Fetching data for {city}...")
        raw_data = fetch_weather_data(city)
        if raw_data:
            processed_record = process_data(raw_data)
            weather_records.append(processed_record)

    # tranform the list of dictionaries into a DataFrame
    df = pd.DataFrame(weather_records)

    # Create the directory if it doesn't exist
    os.makedirs('data/raw', exist_ok=True)

    # Save the DataFrame to a CSV file with a timestamp
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"data/raw/weather_data_{timestamp}.csv"
    
    df.to_csv(filename, index=False)
    print(f"Successfully saved {len(df)} data rows to {filename}")

if __name__ == "__main__":
    main()