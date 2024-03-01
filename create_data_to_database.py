import psycopg2
from psycopg2 import OperationalError

dbname = "master"
user = "postgres"
password = "reah"
host = "localhost"
port = 5432

try:
    # Connect to the database
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    # Create a cursor object
    cur = conn.cursor()
    
    # Create the 'people' table if it doesn't already exist
    cur.execute("""
    CREATE TABLE IF NOT EXISTS people (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        gender VARCHAR(50)
    );
    """)
    
    # Data to insert
    people_data = [
        (1, 'Thareah', 'Male'),
        (2, 'Norak', 'Male'),
        (3, 'Borom', 'Male'),
        (4, 'Ketya', 'Female'),
    ]
    
    # Insert data into the table
    for person in people_data:
        cur.execute("INSERT INTO people (id, name, gender) VALUES (%s, %s, %s)", person)
    
    # Commit the transaction
    conn.commit()
    print("Data inserted successfully.")

except OperationalError as e:
    print(f"Failed to connect to the database: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Ensure the cursor and connection are closed
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals():
        conn.close()
