import psycopg2

def delete_records_by_ids(cur, record_ids):
    # Convert the tuple of IDs into a list of strings for formatting
    ids_str = ','.join(map(str, record_ids))
    query = f"DELETE FROM public.sample WHERE id IN ({ids_str})"
    cur.execute(query)
    print(f"Records with IDs {ids_str} deleted successfully")

def main():
    try:
        # Connect to your PostgreSQL DB
        conn = psycopg2.connect(
            dbname='master',
            user='postgres',
            password='reah',
            host='localhost',
            port='5432'
        )

        # Open a cursor to perform database operations
        cur = conn.cursor()

        # Specify the IDs of the records you want to delete
        record_ids = (6,15)

        # Call the function to delete the records by IDs
        delete_records_by_ids(cur, record_ids)

        # Commit the transaction
        conn.commit()

        # Close the cursor and connection
        cur.close()
        conn.close()

    except Exception as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    main()
