import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.

    def test_negative_age(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "Error (Invalid Age)")

    def test_age_zero(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)

    def test_age_twelve(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def test_age_thirteen(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)

    def test_age_twenty(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_age_twentyone(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    def test_age_sixty(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def test_age_sixtyone(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

if __name__ == '__main__':
    unittest.main()