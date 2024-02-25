import psycopg2

try:
    conn = psycopg2.connect(
        dbname='master',
        user='postgres',
        password='reah',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM public.sample")

    rows = cur.fetchall()

    print(f"{'ID':<5} | {'Name':<20} | {'Gender':<10} | {'Favorite Color':<15}")
    print("-" * 60)

    for row in rows:
        print(f"{row[0]:<5} | {row[1]:<20} | {row[2]:<10} | {row[3]:<15}")

    cur.close()
    conn.close()
except psycopg2.Error as e:
    print("Error connecting to PostgreSQL:", e)
