# 🌦️ Automated Weather Notifier
A Python script that fetches real-time weather data and sends a desktop notification with personalized advice (e.g., "Bring an umbrella").

## Features
- Fetches data from OpenWeatherMap API.
- Uses `.env` for secure configuration.
- Desktop notifications via `plyer`.

## Setup
1. Clone this repo.
2. Install requirements: `pip install -r requirements.txt`
3. Create a `.env` file and add your `WEATHER_API_KEY` and `CITY_NAME`.

## Usage
Run the script using Python:
```bash
python weather_alert.py

* **Prerequisite:** Sign up for a free account at [OpenWeatherMap](https://openweathermap.org/api) to get your API key.
