# 🏥 NHS A&E Informatics Dashboard — Power BI + SQL

This project simulates real NHS Informatics work by analysing A&E (Accident & Emergency) performance data using SQL, Python (SQLite), and Power BI. It demonstrates how healthcare data can be structured, queried, and visualised to track operational targets like the NHS 4-hour performance standard.

---

## 📊 Dashboard Highlights

- **Line Chart** — A&E attendances over time, split by hospital
- **Bar Chart** — Average % of patients seen within 4 hours vs NHS 95% target
- **KPI Card** — Total A&E attendances across both hospitals
- **Slicer** — Dropdown filter to isolate hospital-specific data
- **Interactive Features** — Clickable charts, tooltips, drill modes, slicers
- **Constant Line** — Visual indicator of 95% NHS 4-hour target on bar chart

---

## ⚙️ Tools Used

| Tool         | Purpose                              |
|--------------|---------------------------------------|
| Python       | Generate and populate SQLite database |
| SQLite3      | Store A&E visit data (in `.db` format)|
| ODBC Driver  | Connect Power BI to SQLite            |
| Power BI     | Build and publish interactive visuals |
| SQL          | Query patient flow and performance    |

---

## 🧱 Data Structure

**Table: `ae_visits`**

| Column             | Type     | Description                                  |
|--------------------|----------|----------------------------------------------|
| `id`               | INTEGER  | Auto-increment primary key                   |
| `hospital_name`    | TEXT     | Hospital A / Hospital B                      |
| `visit_date`       | DATE     | Monthly timestamp (e.g. 2023-01-01)          |
| `attendances`      | INTEGER  | Total A&E attendances                        |
| `seen_within_4hrs` | REAL     | % seen within 4 hours (stored as decimals)   |

---

## 🗂 Project Files

- `generate_nhs_data.py` — Python script to generate sample A&E data
- `nhs_ae_visits.db` — SQLite database file used in Power BI
- `NHS_AE_Dashboard.pbix` — Power BI report file
- `PowerBI_SQL_NHS_Project.pdf` — Exported dashboard as PDF

---

## 🎯 Learning Objectives

- Understand how structured data supports NHS operational decision-making
- Build dashboards that surface performance insights from raw data
- Learn how to connect a SQL database to Power BI using ODBC
- Apply data visualisation principles to real-world KPIs

---

## 🧠 Why This Project Matters

This project mirrors the kind of performance-monitoring and business intelligence work done by NHS informatics teams. It highlights your ability to work with relational data, write SQL queries, and present findings in an interactive, stakeholder-ready format.

---

## 📁 Export Options

- The dashboard is published as a PDF for static sharing
- The `.pbix` file can be opened in Power BI Desktop to explore or extend
