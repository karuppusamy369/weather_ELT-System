import requests
from dotenv import load_dotenv
import os
from datetime import datetime
import mysql.connector
import schedule
import time

# Load API key
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# MySQL connection info
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "root"
DB_NAME = "weather_db"

# Cities to fetch
cities = ["London", "New York", "Tokyo"]

# ETL function
def fetch_and_store_weather():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()
        
        for city in cities:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            data = response.json()

            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            weather_desc = data['weather'][0]['description']
            timestamp = datetime.now()

            sql = "INSERT INTO weather_data (city, temperature, humidity, weather_description, timestamp) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (city, temperature, humidity, weather_desc, timestamp))
            print(f"Inserted data for {city} at {timestamp}")
        cursor.execute("select temperature from weather_data")
        row=cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

# Schedule ETL to run every 30 minutes
schedule.every(1).minutes.do(fetch_and_store_weather)

print("Weather ETL automation started...")
fetch_and_store_weather()  
# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)