import requests
from datetime import datetime
import os
import csv

OPENWEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
city_name = "Seoul"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPENWEATHER_API_KEY}"
url += "&units=metric"

response = requests.get(url)
result = response.json()

weather_status = result["weather"][0]["main"]
temp = result["main"]["temp"]
humidity = result["main"]["humidity"]

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# weather.csv 만들기
csv_exist = os.path.exists("weather.csv")


header = ["current_time", "temp", "humidity", "weather_status"]

with open("weather.csv", "a", newline="") as f:
    writer = csv.writer(f)
    if csv_exist == False:
        writer.writerow(header)
    
    writer.writerow([current_time, temp, humidity, weather_status])
        
print("날씨 저장 완료")

