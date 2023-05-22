from flask import Flask, render_template, redirect, url_for, request, json, send_file
import sqlite3 as sql
from sqlite3 import Error
import logging
import resp_gen as RespGen
from datetime import date

logging.basicConfig(filename='record.log', level=logging.DEBUG)

app = Flask(__name__, template_folder='templates')

# def get_db_connection():
#     conn = sql.connect('requests.db')
#     conn.row_factory = sql.Row
#     return conn

@app.route('/', methods=['POST', 'GET'])
def index():

    app.logger.debug("debug log info")
    app.logger.info("Info log information")
    app.logger.warning("Warning log info")
    app.logger.error("Error log info")
    app.logger.critical("Critical log info")

    if request.method == 'POST':

        email_check = request.form['corp_email_input']
        print(email_check)
        current_date = str(date.today())
        conn = sql.connect("requests.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM requests \
                       WHERE email LIKE ? \
                       AND submit_date LIKE ?", (email_check, current_date,))
        email_records = (len(cursor.fetchall()))
        if email_records > 2:
            print('You have reached your submission limit for the day. Try again tomorrow')
            # Trigger email notification to user telling them they will have to wait until tomorrow
            return render_template('index2.html')
        
        try:
            email =  request.form['corp_email_input']
            surveyLink = request.form['survey_id_input']
            respGen = request.form['numb_of_resp_input']
            responseType = request.form['resp_type_select']
            # print(email, surveyLink, respGen, responseType)
             # RespGen.main(email, surveyLink, respGen, responseType)

            if (email != '') and (surveyLink != '') and (respGen != '') and (responseType != ''):
                with sql.connect("requests.db") as conn:
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO requests \
                        (email,surveyurl,respGen,responseType) \
                        VALUES(?,?,?,?)",(email, surveyLink, respGen, responseType))
                    # cursor.execute("SELECT * FROM requests")
                    # print(cursor.fetchall())
                    # conn.close()
                    print("Success!")
                    return
        
        except:
            print("Exception shown.")
            conn.rollback()
            return render_template('error.html')
        
        finally:
            print("Finally")
            conn.commit()
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
    p = 'static/files/CX_Digital_Experience_DataIRL_Temp.qsf'
    return send_file(p, as_attachment=True)

@app.route('/download/ex_can_xp')
def download_ex_can_xp():
    p = 'static/files/EX_Candidate_Experience_Applicant_DataIRL_Temp.qsf'
    return send_file(p, as_attachment=True)

@app.route('/download/ex_em_xp')
def download_ex_em_xp():
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
    # Returns survey link
    return

if __name__ == '__main__':
    app.run(debug=True)