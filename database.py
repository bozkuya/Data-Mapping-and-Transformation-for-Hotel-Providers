import psycopg2
from classes import Category, Chain, Hotel

def upload_to_db(categories, chains, hotels, db_conn):
    # Create a cursor object using the database connection
    cursor = db_conn.cursor()
    
    # Insert each category into the Category table
    for category in categories.values():
        cursor.execute("""
            INSERT INTO Category (Category_ID, Category_Name) 
            VALUES (%s, %s) 
            ON CONFLICT (Category_ID) DO NOTHING
            """, (category.category_id, category.category_name))
    
    # Insert each chain into the Chain table
    for chain in chains.values():
        cursor.execute("""
            INSERT INTO Chain (Chain_ID, Chain_Name) 
            VALUES (%s, %s) 
            ON CONFLICT (Chain_ID) DO NOTHING
            """, (chain.chain_id, chain.chain_name))
    
    # Insert each hotel into the Hotel table
    for hotel in hotels:
        cursor.execute("""
            INSERT INTO Hotel (Hotel_ID, Hotel_Name, Category_ID, Chain_ID, Location) 
            VALUES (%s, %s, %s, %s, POINT(%s, %s)) 
            ON CONFLICT (Hotel_ID) DO NOTHING
            """, (hotel.hotel_id, hotel.hotel_name, hotel.category.category_id, hotel.chain.chain_id, hotel.location["latitude"], hotel.location["longitude"]))
    
    # Commit the transaction
    db_conn.commit()
    # Close the cursor
    cursor.close()