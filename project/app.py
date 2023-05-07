from flask import Flask, render_template, redirect, url_for, request, json, send_file

# Below temp for how to use database
# flask-peewee database, but could be SQLAlchemy instead.
# from flask_peewee.db import Database

# Uncomment below out when ready to run requests
# import resp_gen as RespGen

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        email =  request.form['corp_email_input']
        surveyLink = request.form['survey_id_input']
        respGen = request.form['numb_of_resp_input']
        responseType = request.form['resp_type_select']
        # return json.dumps({'status':'OK','email':email,'surveyLink':surveyLink, 'numOfResponses': numOfResponses, 'responseType':responseType})
        print(email, surveyLink, respGen, responseType)
        RespGen.main(email, surveyLink, respGen, responseType)

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
    p = 'static/files/CX_Customer_Care_DataIRL_Temp.qsf'
    return send_file(p, as_attachment=True)

@app.route('/download/ex_can_xp')
def download_ex_can_xp():
    # Placeholder file
    p = 'static/files/CX_Customer_Care_DataIRL_Temp.qsf'
    return send_file(p, as_attachment=True)

@app.route('/download/ex_em_xp')
def download_ex_em_xp():
    # Placeholder file
    p = 'static/files/CX_Customer_Care_DataIRL_Temp.qsf'
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

# db = Database(app)

if __name__ == '__main__':
    app.run(debug=True)