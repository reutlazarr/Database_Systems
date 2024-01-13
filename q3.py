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
    # We will display the locations from covid_deaths.csv only where the num of new deaths were bigger than the num of new cases
    # We will show location without duplicates using "DISTINCT"
    cursor.execute("""
        SELECT DISTINCT location
        FROM covid_deaths
        WHERE new_deaths > new_cases

    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
