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
    #we will return the date and the amount of new cases only in South America,
    #where there have been more than 150,000 new cases 
    #The result will be ordered by new cases in ascending order using "ORDER BY"
    cursor.execute("""
        SELECT date, new_cases
        FROM covid_deaths
        WHERE location = 'south america' AND new_cases > 150000
        ORDER BY new_cases ASC
        
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
