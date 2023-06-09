import sqlite3

connection = sqlite3.connect('requests.db')

with open('main/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO requests (email, surveyurl, respGen, responseType) VALUES (?, ?, ?, ?)",
            ('email', 'www.qualtrics.com/SV_73243092sdjhbgf', '5', 'cx_customer_care')
            )

cur.execute("INSERT INTO requests (email, surveyurl, respGen, responseType) VALUES (?, ?, ?, ?)",
            ('email', 'www.qualtrics.com/SV_73243092sdjhbgf', '5', 'cx_digital_xp')
            )

connection.commit()
connection.close()