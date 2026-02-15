# 🌦️ Automated Weather Notifier
A Python script that fetches real-time weather data and sends a desktop notification with personalized advice (e.g., "Bring an umbrella").

## Prerequisite
Sign up for a free account at [OpenWeatherMap](https://openweathermap.org/api) to get your API key.

## Features
- Fetches data from OpenWeatherMap API.
- Uses `.env` for secure configuration.
- Desktop notifications via `plyer`.

## Setup
1. Clone this repo.
2. Install requirements: `pip install -r requirements.txt`
3. Create a `.env` file and add your `WEATHER_API_KEY` and `CITY_NAME`.

## 🚀 Automation

To get weather alerts every morning without running the script manually:

### Windows (Task Scheduler)
1. Open **Task Scheduler** and click **Create Basic Task**.
2. Set the Trigger to **Daily** at your preferred time.
3. For **Action**, select **Start a Program**.
4. In **Program/script**, type `pythonw.exe`.
5. In **Add arguments**, paste the full path to `weather_alert.py`.

### macOS/Linux (Cron)
1. Open terminal and type `crontab -e`.
2. Add the following line to run at 8:00 AM daily:
   `00 08 * * * /usr/bin/python3 /absolute/path/to/weather_alert.py`

## Usage
Run the script using Python:
```bash
python weather_alert.py 



