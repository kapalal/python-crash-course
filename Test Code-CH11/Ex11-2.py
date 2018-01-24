# 11-2. Population: Modify your function so it requires a third parameter, population. 
# It should now return a single string of the form City, Country – population xxx, such as Santiago, Chile – population 5000000. 
# Run test_cities.py again. 
# Make sure test_city_country() fails this time.Modify the function so the population parameter is optional.
# Run test_cities.py again, and make sure test_city_country() passes again.
# Write a second test called test_city_country_population() that verifies you can call 
# your function with the values 'santiago', 'chile', and 'population=5000000'. 
# Run test_cities.py again, and make sure this new test passes.

import unittest
from city_functions import get_city

class citypopTestCase(unittest.TestCase):
    """Test for city_functions.py"""

    def test_get_city_pop(self):
        city_info = get_city('milano','italia',population=50000005)
        self.assertEqual(city_info,"Milano,Italia - 50000005")        

unittest.main()
