import pandas as pd
import psycopg2

# Replace these with your Excel file's path and sheet name
excel_file_path = r'C:\Users\User\Downloads\fender_people (1).xlsx'
sheet_name = 'Sheet1'

# Read the Excel file
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

# Database connection parameters - replace these with your details
db_params = {
    "dbname": "master",
    "user": "postgres",
    "password": "reah",
    "host": "localhost",
    "port": "5432"
}


# Connect to your database
conn = psycopg2.connect(**db_params)
cur = conn.cursor()

# Insert each row from the DataFrame
for index, row in df.iterrows():
    cur.execute(
        "INSERT INTO public.sample (name, gender, favorite_color) VALUES (%s, %s, %s)",
        (row['name'], row['gender'], row['favorite_color'])
    )

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
