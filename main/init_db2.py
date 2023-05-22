import sqlite3

connection = sqlite3.connect('requests.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO requests (email, surveyurl, respGen, responseType) VALUES (?, ?, ?, ?)",
            ('email', 'www.qualtrics.com/SV_73243092sdjhbgf', '5', 'CX Customer Experience')
            )

cur.execute("INSERT INTO requests (email, surveyurl, respGen, responseType) VALUES (?, ?, ?, ?)",
            ('email', 'www.qualtrics.com/SV_73243092sdjhbgf', '5', 'CX Digital Experience')
            )

connection.commit()
connection.close()