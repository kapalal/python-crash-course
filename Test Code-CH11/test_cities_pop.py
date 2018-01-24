import unittest
from city_functions import get_city

class citypopTestCase(unittest.TestCase):
    """Test for city_functions.py"""

    def test_get_city_pop(self):
        city_info = get_city('milano','italia',population=50000005)
        self.assertEqual(city_info,"Milano,Italia - 50000005")        

unittest.main()
