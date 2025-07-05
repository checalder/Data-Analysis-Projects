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