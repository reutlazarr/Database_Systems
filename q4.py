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
    # We will present the 20 days in which there were the most new cases in Israel from covid_deaths.csv
    # By using "LIMIT 20" and "ORDER BY - descent"
    cursor.execute("""
        SELECT DISTINCT date, new_cases
        FROM covid_deaths
        WHERE location = 'Israel'
        ORDER BY new_cases DESC
        LIMIT 20

    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
