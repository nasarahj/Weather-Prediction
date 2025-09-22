from weather_data import WeatherData
from sqlweather import WeatherSummary, create_session


def main():
    weather = WeatherData(35.9653, -83.9233, 7, 15)

    weather.find_mean_temp()
    weather.find_max_wind_speed()
    weather.find_precipitation_sum()

    print("\n--- 5-Year Weather Summary for July 15 ---")
    print(f"Mean Temperature (F): {weather.avg_temp:.2f}")
    print(f"Min Temperature (F): {weather.min_temp}")
    print(f"Max Temperature (F): {weather.max_temp}")

    print(f"\nMax Wind Speed (mph): {weather.max_wind}")
    print(f"Avg Wind Speed (mph): {weather.avg_wind}")
    print(f"Min Wind Speed (mph): {weather.min_wind}")

    print(f"\nTotal Precipitation (in): {weather.sum_precip:.2f}")
    print(f"Min Precipitation (in): {weather.min_precip}")
    print(f"Max Precipitation (in): {weather.max_precip}")

# Save results to SQLite database
    session = create_session()

    summary = WeatherSummary(
        latitude=weather.latitude,
        longitude=weather.longitude,
        month=weather.month,
        day=weather.day,
        year=2025,
        avg_temp=weather.avg_temp,
        min_temp=weather.min_temp,
        max_temp=weather.max_temp,
        avg_wind=weather.avg_wind,
        min_wind=weather.min_wind,
        max_wind=weather.max_wind,
        sum_precip=weather.sum_precip,
        min_precip=weather.min_precip,
        max_precip=weather.max_precip
    )

    session.add(summary)
    session.commit()
    # Query and print saved data for verification (Part C6)
    print("\n--- Retrieved Data from Database ---")
    result = session.query(WeatherSummary).filter_by(
        latitude=weather.latitude,
        longitude=weather.longitude,
        month=weather.month,
        day=weather.day,
        year=2025
    ).first()

    if result:
        print(f"Date: {result.month}/{result.day}/{result.year}")
        print(f"Avg Temp: {result.avg_temp:.2f} F")
        print(f"Min Temp: {result.min_temp} F")
        print(f"Max Temp: {result.max_temp} F")
        print(f"Avg Wind: {result.avg_wind:.2f} mph")
        print(f"Min Wind: {result.min_wind} mph")
        print(f"Max Wind: {result.max_wind} mph")
        print(f"Total Precip: {result.sum_precip:.2f} in")
        print(f"Min Precip: {result.min_precip} in")
        print(f"Max Precip: {result.max_precip} in")
    else:
        print("⚠️ No matching record found in the database.")

    print("\n✅ Weather data successfully saved to the database.")

if __name__ == "__main__":
    main()



