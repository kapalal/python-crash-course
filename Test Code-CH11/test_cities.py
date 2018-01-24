import unittest
from city_functions import get_city

class cityTestCase(unittest.TestCase):
    """Test for city_functions.py"""

    def test_get_city(self):
        city_info = get_city('milano','italia')
        self.assertEqual(city_info,"Milano,Italia")        

unittest.main()

