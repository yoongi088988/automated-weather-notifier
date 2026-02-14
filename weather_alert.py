import os
from dotenv import load_dotenv

load_dotenv()

import requests
from plyer import notification

# 1. Configuration
API_KEY = os.getenv("WEATHER_API_KEY")
CITY = os.getenv("CITY_NAME")
# Using Metric units makes the math easier!
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def get_weather():
    try:
        response = requests.get(URL)
        data = response.json()
        
        if data["cod"] == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]

            # ==== newly added section ====
            if "rain" in desc.lower():
                advice = "☔ Grab an umbrella before you head out!"
            elif temp>30:
                advice ="☀️ It's a scorcher! Stay hydrated."
            else:
                advice = "✅ Have a great day!"

            # =============================
            
            # 2. Create the message
            message = f"It's {temp}°C with {desc} in {CITY}.\n{advice}."
            
            # 3. Send Notification
            notification.notify(
                title=f"Weather Update: {CITY}",
                message=message,
                app_icon=None,  # You can add a .ico file path here
                timeout=10      # Seconds the notification stays on screen
            )
        else:
            print("City not found!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_weather()