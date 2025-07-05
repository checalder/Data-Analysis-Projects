import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect("air_quality.db")
cursor = conn.cursor()

# cursor.execute('''
# DROP TABLE cities''')

cursor.executescript('''
               DROP TABLE cities;
               CREATE TABLE cities(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               city_name TEXT,
               measurement_date DATE,
               pm25 REAL,
               pm10 REAL,
               no2 REAL
               )
               ''')



cities = ["London", "Manchester", "Bristol", "Leeds", "Birmingham"]

#strptime parses string into pyton date object
start_date = datetime.strptime("2020-10-21", "%Y-%m-%d")# the % symbol indicates where the values are located in the string before it, it indicates the format of the previous string in other words

#for every city, add a tuple to the table with its info
#loop this process for a 30 day period
#use the random module to genereate values
for day in range(30):
    for city in cities:

        date = start_date + timedelta(day)
        pm25 = round(random.uniform(10,40), 2)
        pm10 = round(random.uniform(20,60), 2)
        no2 = round(random.uniform(30, 80), 2)

        cursor.execute('''
        INSERT INTO cities(city_name, measurement_date, pm25, pm10, no2) VALUES(?,?,?,?,?)''',
        (city, date.strftime("%Y-%m-%d"), pm25, pm10, no2))


conn.commit()
conn.close()