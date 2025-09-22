import unittest
from weather_data import WeatherData

class TestWeatherData(unittest.TestCase):

    def setUp(self):
        self.weather = WeatherData(35.9653, -83.9233, 7, 15)

    def test_years_list(self):
        self.assertEqual(len(self.weather.years), 5)
        self.assertTrue(all(isinstance(year, int) for year in self.weather.years))

    def test_fetch_weather_data_structure(self):
        data = self.weather.fetch_weather_data(self.weather.years[0])
        self.assertIsInstance(data, dict)
        self.assertIn("temp", data)
        self.assertIn("wind", data)
        self.assertIn("precip", data)

    def test_temperature_type(self):
        data = self.weather.fetch_weather_data(self.weather.years[0])
        self.assertIsInstance(data["temp"], (int, float))

if __name__ == "__main__":
    unittest.main()
