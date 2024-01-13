import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="covid_db",
        port='3307',
    )
    cursor = mydb.cursor()
    # We will display the names of the locations from covid_deaths.csv without duplicates locations using "DISTINCT"
    cursor.execute("""
        SELECT DISTINCT location 
        FROM covid_deaths
        """)
    print(', '.join(str(row) for row in cursor.fetchall()))
