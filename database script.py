import sqlite3
from datetime import datetime, timedelta
import random

connection = sqlite3.connect('nhs_ae_visits.db')
#connects the database to our python script

cursor = connection.cursor()
#acts as our navigator, where we are working, think the blinking line that indicates where you will next type, cursor
#From Latin "cursor" — meaning "runner".

# Comes from the verb "currere", meaning "to run".

# Originally:

# A cursor was someone or something that moves along a path — literally a “runner.”

# In modern computing:

# A cursor "moves" through data (rows in a result set, lines of text, screen coordinates), just like a runner moves forward.

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ae_visits(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hospital_name TEXT,
    visit_date DATE,
    attendances INTEGER,
    seen_within_4hrs REAL
)''')

cursor.execute('DELETE FROM ae_visits')

hospitals = ['Hospital A', 'Hospital B']
start_date = datetime(2023, 1, 1)



for i in range(12):  # 12 months
    for hospital in hospitals:
        #strftime creates a string from a time object and formats it in long years %Y 2025 as opposed to short years %y 25, the % tells
        #tells us its a format, not entirely sure but theres something similar in C but alot of coding languages have this rule
        date = (start_date + timedelta(days=30 * i)).strftime('%Y-%m-%d')

        attendances = random.randint(70, 150)
        #uniform generates a float(number with a decimal), and round is to whatever decimal place, this case 1
        seen_within_4hrs = round(random.uniform(60, 98), 1)/100
        

        cursor.execute('''
            INSERT INTO ae_visits (hospital_name, visit_date, attendances, seen_within_4hrs)
            VALUES (?, ?, ?, ?)
        ''', (hospital, date, attendances, seen_within_4hrs))



cursor.execute('SELECT * FROM ae_visits')
i = 0
for row in cursor.fetchall():
    i=i+1
    print(row)
    print(i)

connection.commit()
connection.close()