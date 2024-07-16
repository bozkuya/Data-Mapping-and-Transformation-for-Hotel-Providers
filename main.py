import json
import psycopg2
from data_migration import parse_data
from database import upload_to_db

def main():
    # JSON dosyasını oku
    with open('example_hotel_data.json', 'r') as file:
        json_data = json.load(file)
    
    # JSON verilerini ayrıştır
    categories, chains, hotels = parse_data(json_data)
    
    # Veritabanı bağlantısını kur
    # Burada kendi bilgilerinizi girerek işlem yapabilirsiniz.
    db_conn = psycopg2.connect(
        dbname="your_db",
        user="your_user",
        password="your_password",
        host="your_host",
        port="your_port"
    )
    
    # Verileri veritabanına yükle
    upload_to_db(categories, chains, hotels, db_conn)
    
    # Veritabanı bağlantısını kapat
    db_conn.close()

if __name__ == '__main__':
    main()