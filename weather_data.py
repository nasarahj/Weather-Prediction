import requests
from datetime import datetime

class WeatherData:
    def __init__(self, latitude, longitude, month, day):
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day = day

        current_year = datetime.now().year
        self.years = [current_year - i for i in range(1, 6)]

        # Initialize lists to store yearly data
        self.temps = []
        self.wind_speeds = []
        self.precip_totals = []

        # Initialize result attributes
        self.avg_temp = None
        self.min_temp = None
        self.max_temp = None

        self.avg_wind = None
        self.min_wind = None
        self.max_wind = None

        self.sum_precip = None
        self.min_precip = None
        self.max_precip = None

    def fetch_weather_data(self, year):
        date_str = f"{year}-{self.month:02d}-{self.day:02d}"
        url = (
            f"https://archive-api.open-meteo.com/v1/archive?"
            f"latitude={self.latitude}&longitude={self.longitude}"
            f"&start_date={date_str}&end_date={date_str}"
            f"&daily=temperature_2m_mean,wind_speed_10m_max,precipitation_sum"
            f"&temperature_unit=fahrenheit"
            f"&timezone=America/New_York"
        )
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "daily" in data and data["daily"]["time"]:
                return {
                    "temp": data["daily"]["temperature_2m_mean"][0],
                    "wind": data["daily"]["wind_speed_10m_max"][0],
                    "precip": data["daily"]["precipitation_sum"][0]
                }
        else:
            print(f"Failed for {date_str}: {response.status_code}")
        return None

    def find_mean_temp(self):
        for year in self.years:
            data = self.fetch_weather_data(year)
            if data:
                self.temps.append(data["temp"])

        if self.temps:
            self.avg_temp = sum(self.temps) / len(self.temps)
            self.min_temp = min(self.temps)
            self.max_temp = max(self.temps)

    def find_max_wind_speed(self):
        for year in self.years:
            data = self.fetch_weather_data(year)
            if data:
                self.wind_speeds.append(data["wind"])

        if self.wind_speeds:
            self.avg_wind = sum(self.wind_speeds) / len(self.wind_speeds)
            self.min_wind = min(self.wind_speeds)
            self.max_wind = max(self.wind_speeds)

    def find_precipitation_sum(self):
        for year in self.years:
            data = self.fetch_weather_data(year)
            if data:
                self.precip_totals.append(data["precip"])

        if self.precip_totals:
            self.sum_precip = sum(self.precip_totals)
            self.min_precip = min(self.precip_totals)
            self.max_precip = max(self.precip_totals)
