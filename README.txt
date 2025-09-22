Weather Data Collection Project

How to Run the Program
1. Make sure Python 3 is installed.
2. Install required libraries using:
   pip install -r requirements.txt
3. Run the program using:
   python main.py

Program Overview
This program:
- Fetches 5 years of historical weather data for Knoxville, TN (July 15).
- Calculates mean temp, wind speed, and precipitation.
- Stores the data in a local SQLite database using SQLAlchemy.
- Runs unit tests to confirm functions work.

Files Included
- weather_data.py – Fetches weather data from API
- sqlweather.py – SQLAlchemy ORM for database table
- main.py – Runs the program
- test.py – Unit tests
- requirements.txt – Required packages
- README.txt – Instructions
- weather_data.db – SQLite database (after first run)

