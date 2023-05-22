import sqlite3 as sql

connection = sql.connect("requests.db")

cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS requests
                (date TEXT, requestid INT, email TEXT, surveyLink Text, respGen INT, responseType Text)""")

# cursor.execute("""CREATE TABLE IF NOT EXISTS ERRORLOG
#                 (date TEXT, requestid INT, email TEXT, surveyLink Text, respGen INT, responseType Text)""")

connection.commit()
connection.close()