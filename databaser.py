# Import the SQLite3 module for database operations
import sqlite3
# Import datetime for handling dates
import datetime
# Import random for generating mock data
import random

# Connect to a SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("efficiency_tracker")

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Drop existing tables if they exist (reset the database)
cur.executescript('''DROP TABLE IF EXISTS appointments;
                  DROP TABLE IF EXISTS clinics;
                  DROP TABLE IF EXISTS wait_times;''')

# Create 'appointments' table to store patient appointments
cur.executescript('''

    CREATE TABLE IF NOT EXISTS appointments(
            appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id TEXT,
            clinic_name TEXT,
            appointment_date DATE,
            status TEXT,
            referral_source TEXT
        );
''')

# Create 'clinics' table to define clinic capacity and department
cur.execute('''

    CREATE TABLE IF NOT EXISTS clinics(
            clinic_name TEXT PRIMARY KEY,
            department TEXT,
            avg_capacity_per_day INT
        )
''')

# Create 'wait_times' table to store referral and appointment dates
cur.execute('''

    CREATE TABLE IF NOT EXISTS wait_times(
            patient_id TEXT,
            referral_date DATE,
            appointment_date DATE)
''')

# Define possible appointment outcomes
statuses = ["DNA", "Attended", "Cancelled"]
# Define possible referral sources
referrals = ["GP", "A&E", "Emergency Services", "Triage", "Self"]
# List of mock clinic names
clinics = ["St Georges", "Paddy's Hospital", "Red Cross South", "Red Cross North", "Divine Saviour's Allegiance of the Holy Ninth Order Parish"]
# List of medical departments associated with each clinic
departments = ["Emergency", "Cardiology", "Neurology", "Orthopedics", "Urology", "Endocrinology", "ENT"]

# Number of mock appointment entries to generate
entries = 100

# Generate mock appointment entries
for i in range(entries):
    patient_id = f"PAT{random.randint(1,999)}"
    clinic_name = clinics[random.randint(0,4)]
    appointment_date = datetime.date.today() - datetime.timedelta(random.randint(1, 10))
    status = statuses[random.randint(0, 2)]
    referral_source = referrals[random.randint(0,4)]

# Insert a mock appointment record into the database
    cur.execute('''

        INSERT INTO appointments(patient_id, clinic_name, appointment_date, status, referral_source)
        VALUES (?,?,?,?,?)''',(patient_id, clinic_name, appointment_date.strftime("%Y-%m-%d"), status, referral_source)
        )

# Insert one clinic entry per name with random capacity
for i in range(len(clinics)):
    department = departments[i]
    avg_capacity_per_day = random.randint(30,100)
    cur.execute('''
        INSERT INTO clinics(clinic_name, department, avg_capacity_per_day)
        VALUES(?,?,?)''',(clinics[i], department, avg_capacity_per_day))

# Fetch all appointments to use in generating wait_times
appointments = cur.execute('''
SELECT patient_id, appointment_date FROM appointments
''').fetchall()

# For each appointment, generate a referral date and insert a wait time
for i in range(len(appointments)):
    appointment_date = appointments[i][1]#get date in string format
    referral_date = (datetime.datetime.strptime(appointment_date, "%Y-%m-%d") - datetime.timedelta(random.randint(0,10))).strftime("%Y-%m-%d")
    patient_id = appointments[i][0]

    cur.execute('''
    INSERT INTO wait_times(patient_id, referral_date, appointment_date)
    VALUES(?,?,?)''', (patient_id, referral_date, appointment_date))


# Commit all changes to the database
conn.commit()
# Close the database connection
conn.close()