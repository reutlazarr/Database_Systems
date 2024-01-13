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
    # We will return the date and the amount of new cases order by ascending order using "ORDER BY"
    # We will return only the cases in South America where there were more than 15000 new cases per day
    cursor.execute("""
        SELECT date, new_cases
        FROM covid_deaths
        WHERE location = 'south america' AND new_cases > 150000
        ORDER BY new_cases ASC
        
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
