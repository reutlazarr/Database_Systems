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
    # We will present the dates, locations and new cases where the num of new cases were equal to the num of weekly hospital admissions,
    # When the weekly hospital admissions were bigger than 0. 
    # We will display it by descent order using "ORDER By"
    cursor.execute("""
        SELECT date, location, new_cases
        FROM covid_deaths
        WHERE new_cases = weekly_hosp_admissions AND weekly_hosp_admissions > 0
        ORDER BY new_cases DESC

    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
