import sqlite3

# Define database
database_name = 'properties.db'

def create_database():
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS properties (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        address TEXT,
        suburb TEXT,
        state TEXT,
        post_code TEXT,
        price TEXT,
        property_type TEXT,
        bed TEXT,
        bath TEXT,
        parking TEXT
    )
    ''')

    connection.commit()
    connection.close()  

def insert_property(address, suburb, state, post_code, price, property_type, bed, bath, parking):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    cursor.execute('''
    INSERT INTO properties (address, suburb, state, post_code, price, property_type, bed, bath, parking)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (address, suburb, state, post_code, price, property_type, bed, bath, parking))

    connection.commit()
    connection.close()

if __name__ == '__main__':
    create_database()