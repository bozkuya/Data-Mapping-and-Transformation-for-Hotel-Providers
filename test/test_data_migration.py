import unittest
from data_migration import parse_data

class TestDataMigration(unittest.TestCase):
    def test_parse_data(self):
        json_data = {
            "0": {"property_id": 10000527, "category": {"id": "1", "name": "Hotel"}, "chain": {"id": "0", "name": "Independent"}, "location": {"coordinates": {"latitude": 42.60803, "longitude": 8.864105}}, "name": "hotel 0"}
        }
        categories, chains, hotels = parse_data(json_data)
        self.assertEqual(len(categories), 1)
        self.assertEqual(len(chains), 1)
        self.assertEqual(len(hotels), 1)
        self.assertEqual(hotels[0].hotel_name, "hotel 0")

if __name__ == '__main__':
    unittest.main()