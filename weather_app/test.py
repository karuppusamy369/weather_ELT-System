import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env

API_KEY = os.getenv("OPENWEATHER_API_KEY")  # Use the variable name, not the key itself

if API_KEY is None:
    raise ValueError("API_KEY not loaded. Check your .env file!")

print("API Key loaded successfully:", API_KEY)

city="London"
url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response=requests.get(url)
data=response.json()
temp=data['main']['temp']
hum=data['main']['humidity']
weathers=data['weather'][0]['description']
print(f"City: {city}")
print(f"temperature: {temp} C")
print(f"humidity: {hum}%")
print(f"weather:{weathers}")