import unittest
from classes import Category, Chain, Hotel

class TestCategory(unittest.TestCase):
    def test_category_creation(self):
        category = Category(category_id=1, category_name="Hotel")
        self.assertEqual(category.category_id, 1)
        self.assertEqual(category.category_name, "Hotel")

class TestChain(unittest.TestCase):
    def test_chain_creation(self):
        chain = Chain(chain_id=0, chain_name="Independent")
        self.assertEqual(chain.chain_id, 0)
        self.assertEqual(chain.chain_name, "Independent")

class TestHotel(unittest.TestCase):
    def test_hotel_creation(self):
        category = Category(category_id=1, category_name="Hotel")
        chain = Chain(chain_id=0, chain_name="Independent")
        location = {"latitude": 42.60803, "longitude": 8.864105}
        hotel = Hotel(hotel_id=10000527, hotel_name="hotel 0", category=category, chain=chain, location=location)
        self.assertEqual(hotel.hotel_id, 10000527)
        self.assertEqual(hotel.hotel_name, "hotel 0")
        self.assertEqual(hotel.category, category)
        self.assertEqual(hotel.chain, chain)
        self.assertEqual(hotel.location, location)

if __name__ == '__main__':
    unittest.main()