import sqlite3
import matplotlib.pyplot as plt
import pandas as pd


connection = sqlite3.connect("air_quality.db")
cursor = connection.cursor()

#SELECT ALWAYS DETERMINES THE COLUMNS THAT WILL BE EXTRACTED

# Common SQL aggregate functions include:

# AVG() — calculates the average value.
# SUM() — calculates the total sum.
# COUNT() — counts the number of rows.
# MIN() — finds the minimum value.
# MAX() — finds the maximum value.
# GROUP_CONCAT() — concatenates values from a group (SQLite-specific).
# You use these with GROUP BY to summarize data for each group.

# Other useful SQL functions:

# ROUND() — round a numeric value
# UPPER() / LOWER() — convert text to upper/lower case
# LENGTH() — length of a string
# SUBSTR() — substring extraction
# ABS() — absolute value
# DATE() / DATETIME() — date/time manipulation (SQLite and others)


#group by changes the whole way prompts are executed


q1 = cursor.execute('''
    SELECT city_name, round(AVG(pm25),2) AS avg_pm25
    FROM cities
    GROUP BY city_name
    ORDER BY avg_pm25 DESC
''')

#fetchall returns data type: list of tuples
print(q1.fetchall())
print("\n\n")

q2 = cursor.execute('''
    SELECT *
    FROM cities
    WHERE pm25 > 25 OR pm10 > 50 OR no2 > 40  
    ORDER BY measurement_date  
''')

print(q2.fetchall())
print("\n\n")


q3 = cursor.execute('''
    SELECT *
    FROM cities
    WHERE pm25 < 25 AND pm10 < 50 AND no2 < 40
    ORDER BY measurement_date
''')


print(q3.fetchall())
print('\n\n')


q4 = cursor.execute('''
    SELECT measurement_date, ROUND(AVG(pm25), 2) AS avg_pm25
    FROM cities
    GROUP BY measurement_date
    ORDER BY measurement_date
''')

#basically, aggregate functions like AVG etc are only applied when you use the group keyword, so for each group of values with matching measurement dates, average them into a single value
#group by matching measurement date, then avg the group into a single row for their avg pm_25

#you can group by measurement_date without selecting it in your SELECT statement.
#The grouping will still happen based on measurement_date, but the result will not display the measurement_date column—it will only show the columns you select.

#order then orders the entire query
#here is the average for all the cities 5 > 1 averaging

print(q4.fetchall())
print("\n\n")


df_avg_pm25 = pd.DataFrame(q4.fetchall(), columns=['city_name', 'avg_pm25'])#define the columns


#matplotlib and pandas have innate cross functionality
#so convert your data into a pd.dataframe

plt.figure()


plt.bar(df_avg_pm25['city_name'], df_avg_pm25['avg_pm25'])#DataFrame object has overloaded operators allowing the [] operator to be used like a normal function call
#this is because the class has a ___getitem___ method defined - this is how you overload operators on your methods
#this method then operates like a 2d array/dictionary (basically the same thing, but you cant access arrays using strings? so maybe thats why its a cross between them?)
#then returns a pandas series data type (basically a list), ik they just adding random shit at this point

# ican even create a subgrouping from the data frame by giving a list of colum names into the dataframe like so
#subDF = DF[['city_name', 'avg_pm25]]
#no ___getitem___ will return the new dataframe object

plt.title('Average PM2.5 by City')
plt.xlabel('City')
plt.ylabel('Average PM2.5 (µg/m³)')
plt.xticks(rotation=45)  # rotates city names for readability
plt.tight_layout()       # makes sure labels/titles don’t get cut off
plt.show()

connection.commit()
connection.close()