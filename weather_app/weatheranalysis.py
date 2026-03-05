import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",  
    database="weather_db"
)
cursor = conn.cursor(dictionary=True) 

# Fetch all weather data
cursor.execute("SELECT * FROM weather_data ORDER BY timestamp ASC")
rows = cursor.fetchall()

# Close connection
cursor.close()
conn.close()

# Convert to DataFrame
df = pd.DataFrame(rows)
print(df.head())
plt.figure(figsize=(12,6))

for city in df['city'].unique():
    city_data = df[df['city'] == city]
    plt.plot(city_data['timestamp'], city_data['temperature'], label=city)

plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trends by City")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.figure(figsize=(12,6))

for city in df['city'].unique():
    city_data = df[df['city'] == city]
    plt.plot(city_data['timestamp'], city_data['humidity'], label=city)

plt.xlabel("Time")
plt.ylabel("Humidity (%)")
plt.title("Humidity Trends by City")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

