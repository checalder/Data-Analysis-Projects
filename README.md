# 🌍 City Air Quality Tracker

A Python + SQLite project that simulates environmental monitoring of air pollution across major UK cities. This project builds real-world skills in SQL, data analysis, and data visualization.

---

## 📊 Project Overview

This project tracks PM2.5, PM10, and NO₂ pollution across several UK cities over a 30-day period. Data is stored in SQLite, queried using SQL, analyzed with pandas, and visualized using matplotlib.

---

## 🗃️ Database Schema

**Table: `city_air_data`**

| Column             | Type     | Description                                  |
|--------------------|----------|----------------------------------------------|
| `id`               | INTEGER  | Unique row ID                                |
| `city_name`        | TEXT     | Name of the city                             |
| `measurement_date` | DATE     | Date of pollution reading                    |
| `pm25`             | REAL     | Fine particles ≤ 2.5μm                       |
| `pm10`             | REAL     | Coarse particles ≤ 10μm                      |
| `no2`              | REAL     | Nitrogen dioxide level (μg/m³)               |

---

## 🔧 Features

- Random pollution data generation for 5 cities
- SQL queries for:
  - City-wise average PM2.5
  - WHO threshold exceedances
  - Daily pollution trends
- Visualization:
  - Bar chart for average PM2.5 per city
  - Line chart for daily PM2.5 average
- Data manipulation using pandas

---

## 📚 Tech Stack

- Python 3
- SQLite
- pandas
- matplotlib
- datetime, random

---

## 🚀 How to Run

1. Clone this repo
2. Ensure Python and pip are installed
3. Install dependencies:
   ```
   pip install pandas matplotlib
   ```
4. Run the script (`main.py`) to populate the database and generate plots
5. Open `air_quality.db` in DB Browser or analyze via code

# Data Analysis Projects – Central Hub

Welcome to my collection of hands-on data analysis projects. Each one explores real-world datasets using tools like SQL, Power BI, and Python — showing how data can be used to tell compelling stories, spot trends, and support decision-making.

---

## 📊 [City Air Quality Tracker](https://github.com/checalder/Data-Analysis-Projects/tree/Air-Quality-Dashboard)

A data project focused on monitoring air pollution across UK cities. It includes:

- A custom SQLite database storing nitrogen dioxide (NO₂) levels
- SQL queries for trends and hotspot detection
- Python analysis and optional visualisations

> This dashboard explores how environmental data can help us understand public health risks and urban planning priorities.

---

## 🏥 [NHS A&E Dashboard](https://github.com/checalder/Data-Analysis-Projects/tree/Hospital-Tracker)

A mini analytics project inspired by NHS Informatics workflows. It demonstrates:

- SQL querying of A&E attendance data from two hospitals
- A Power BI dashboard with KPIs, filters, and NHS 4-hour target tracking
- Use of industry tools to simulate real-world reporting

> Built as part of my preparation for the NHS Informatics Work Placement Scheme 2025.
