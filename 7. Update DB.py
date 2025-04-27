import pandas as pd
import mysql.connector

!service mysql start

# Load CSV file into a DataFrame
df = pd.read_csv('output.csv')

# Convert 'time' column to time format
df['time'] = pd.to_datetime(df['time']).dt.time

# Database connection
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost', #enter host of your system
        user='root',    #enter user of your system
        password='root123', #enter password of your system
        database='mydatabase'
    )
    return conn

# Insert data into MySQL
def insert_data(df):
    conn = get_db_connection()
    cur = conn.cursor()

    for index, row in df.iterrows():
        cur.execute(
            'INSERT INTO attendance (name, time) VALUES (%s, %s)',
            (row['name'], row['time'])
        )

    conn.commit()
    cur.close()
    conn.close()

# Run the insertion function
insert_data(df)

print("Data inserted successfully.")

!mysql -u root -p'root123' -e "USE mydatabase; select * from attendance;"