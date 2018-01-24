import unittest
from Employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.gianni = Employee('Ivan','Kapalala',500) 
    def test_default_pay(self):
        self.gianni.info()
    def test_raise(self):
        self.gianni.give_raise(18181818)
        self.gianni.info()

unittest.main()