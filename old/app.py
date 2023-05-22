from flask import Flask, render_template, redirect, url_for, request, json, send_file
import sqlite3 as sql
from sqlite3 import Error
import logging
# import init_db as db
# import requests as db

# Below temp for how to use database
# flask-peewee database, but could be SQLAlchemy instead.
# from flask_peewee.db import Database

# Uncomment below out when ready to run requests
import resp_gen as RespGen

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':

        conn = sql.connect("requests.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS REQUESTS \
                    (date TEXT, requestid TEXT, email TEXT, surveyLink Text, respGen TEXT, responseType TEXT)")
        
        try:
            email =  request.form['corp_email_input']
            surveyLink = request.form['survey_id_input']
            respGen = request.form['numb_of_resp_input']
            responseType = request.form['resp_type_select']
            # return json.dumps({'status':'OK','email':email,'surveyLink':surveyLink, 'numOfResponses': numOfResponses, 'responseType':responseType})
            print(email, surveyLink, respGen, responseType)
             # RespGen.main(email, surveyLink, respGen, responseType

            with sql.connect("requests.db") as users:
                cursor = users.cursor()
                cursor.execute("INSERT INTO REQUESTS \
                    (email,surveyLink,respGen,responseType) \
                    VALUES(?,?,?,?)",(email, surveyLink, respGen, responseType))
                cursor.execute("SELECT * FROM REQUESTS")
                print(cursor.fetchall())
                users.commit()
                users.close()
                print("Success!")
                return render_template('index2.html')

            # RespGen.main(email, surveyLink, respGen, responseType)

            # conn = sql.connect("requests.db")
            # with sql.connect("requests.db") as users:
            #     cursor = users.cursor()
            #     cursor.execute("INSERT INTO REQUESTS \
            #         (email,surveyLink,respGen,responseType) \
            #         VALUES(?,?,?,?)",(email, surveyLink, respGen, responseType))
            #     users.commit()
            #     users.close()
            #     print("Success!")
            #     return "Pass"
        
        except:
            print("Something went wrong...error in insert operation")
            users.rollback()
            return "Pass"
        
        # except sql.Error as error:
        #     print("Failed to insert data into sqlite table", error)

        finally:
            print("Finally")
            conn.close()
            return "Pass"

    else:
        return render_template('index2.html')

@app.route('/documentation')
def documentation():
    return render_template('documentation.html')

@app.route('/download/cx_cust_care')
def download_cx_cust_care():
    p = 'static/files/CX_Customer_Care_DataIRL_Temp.qsf'
    return send_file(p, as_attachment=True)


@app.route('/download/cx_digital_xp')
def download_cx_digital_xp():
    # Placeholder file
    p = 'static/files/CX_Digital_Experience_DataIRL_Temp.qsf'
    return send_file(p, as_attachment=True)

@app.route('/download/ex_can_xp')
def download_ex_can_xp():
    # Placeholder file
    p = 'static/files/EX_Candidate_Experience_Applicant_DataIRL_Temp.qsf'
    return send_file(p, as_attachment=True)

@app.route('/download/ex_em_xp')
def download_ex_em_xp():
    # Placeholder file
    p = 'static/files/EX_Employee_Experience_DataIRL_Temp.qsf'
    return send_file(p, as_attachment=True)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/roadmap')
def roadmap():
    return render_template('roadmap.html')

@app.route('/changelog')
def changelog():
    return render_template('changelog.html')

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/feedback')
def feedback():
    # Insert Qualtrics survey link
    return

# @app.route('/list')
# def list():
#    con = sql.connect("database.db")
#    con.row_factory = sql.Row
   
#    cur = con.cursor()
#    cur.execute("select * from students")
   
#    rows = cur.fetchall();
#    return render_template("list.html",rows = rows)


if __name__ == '__main__':
    app.run(debug=True)