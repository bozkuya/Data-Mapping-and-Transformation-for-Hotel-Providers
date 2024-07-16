import unittest
from unittest.mock import Mock, patch
from database import upload_to_db
from classes import Category, Chain, Hotel

class TestDatabase(unittest.TestCase):
    @patch('psycopg2.connect')
    def test_upload_to_db(self, mock_connect):
        # Mock the database connection and cursor
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Create sample data
        categories = {
            "1": Category(category_id=1, category_name="Hotel")
        }
        chains = {
            "0": Chain(chain_id=0, chain_name="Independent")
        }
        hotels = [
            Hotel(hotel_id=10000527, hotel_name="hotel 0", category=categories["1"], chain=chains["0"], location={"latitude": 42.60803, "longitude": 8.864105})
        ]

        # Call the function to test
        upload_to_db(categories, chains, hotels, mock_conn)

        # Assert the expected calls were made to the cursor
        mock_cursor.execute.assert_any_call("""
            INSERT INTO Category (Category_ID, Category_Name) 
            VALUES (%s, %s) 
            ON CONFLICT (Category_ID) DO NOTHING
            """, (1, "Hotel"))

        mock_cursor.execute.assert_any_call("""
            INSERT INTO Chain (Chain_ID, Chain_Name) 
            VALUES (%s, %s) 
            ON CONFLICT (Chain_ID) DO NOTHING
            """, (0, "Independent"))

        mock_cursor.execute.assert_any_call("""
            INSERT INTO Hotel (Hotel_ID, Hotel_Name, Category_ID, Chain_ID, Location) 
            VALUES (%s, %s, %s, %s, POINT(%s, %s)) 
            ON CONFLICT (Hotel_ID) DO NOTHING
            """, (10000527, "hotel 0", 1, 0, 42.60803, 8.864105))

        # Assert commit was called
        mock_conn.commit.assert_called_once()
        # Assert cursor and connection were closed
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()