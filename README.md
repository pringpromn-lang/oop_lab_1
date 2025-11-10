# OOP Lab 1 — Data Processing

## Lab Overview
This lab demonstrates transitioning from procedural to object-oriented programming in Python.  
It uses classes to load, filter, and aggregate city temperature data from a CSV file.

## Project Structure
oop_lab_1/
│
├── README.md # This file
├── Cities.csv # Dataset containing city, country, and temperature
└── data_processing.py # OOP-style code for data processing

## Design Overview

### **Class: DataLoader**
- **Purpose:** Handles reading CSV files and returning data as a list of dictionaries.
- **Methods:**
  - `__init__(base_path=None)`: Sets up a base path for data files.
  - `load_csv(filename)`: Loads a CSV file into a list of dictionaries.

### **Class: Table**
- **Purpose:** Represents tabular data and supports filtering and aggregation.
- **Attributes:**
  - `name`: Table name.
  - `table`: A list of dictionaries (rows).
- **Methods:**
  - `filter(condition)`: Returns a new `Table` containing only rows that meet a lambda condition.
  - `aggregate(func, key)`: Applies a function (like `sum`, `max`, or `len(set())`) on a specific key.

## How to Test and Run
1. Place `Cities.csv` and `data_processing.py` in the same directory.
2. Run the program:
   ```bash
   python data_processing.py
3. Observe the console output:
    Average temperature of all cities
    Cities in Germany and Spain 
    Number of unique countries
    Average temperature for Germany
    Maximum temperature for Italy