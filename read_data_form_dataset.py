import psycopg2

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
    
    # Execute a SELECT statement to retrieve all data from the 'people' table
    cur.execute("SELECT id, name, gender FROM people;")
    
    # Fetch all rows from the query result
    records = cur.fetchall()
    
    # Print header
    print(f"{'id':<4} | {'name':<20} | {'gender'}")
    print("-" * 35)
    
    # Iterate over the rows and print each one
    for record in records:
        id, name, gender = record
        print(f"{id:<4} | {name:<20} | {gender}")
    
except psycopg2.Error as e:
    print(f"Database error: {e}")
finally:
    # Ensure the cursor and connection are closed
    if cur:
        cur.close()
    if conn:
        conn.close()
