from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
import mysql.connector

app = Flask(__name__, 
        static_url_path='',
        static_folder='static',
        template_folder='templates')


@app.route('/')
def direct_form():
    return render_template('direct_form.html')

@app.route('/internal/submit', methods = ['POST'])
def direct_submit():
    cnx = mysql.connector.connect(user='webapp', password='novovoom1web', host='db', database='NovoVoom')
    cursor = cnx.cursor(buffered=True)
    form_data = request.form
    last_name = form_data['last']

    query = "SELECT first, last, dept, phone FROM Employee WHERE last = '" + last_name + "'";
    
    q_list = query.split(';')
    for q in q_list:
        if (len(q) > 2):
            cursor.execute(q) 

    cnx.commit()

    output_str = ""
    for data in cursor:
        for item in data:
            output_str = output_str + str(item) + ",   "
        output_str = output_str + "\n"

    return render_template('results.html', output = output_str)

@app.route('/insert')
def insert_matt():
    cnx = mysql.connector.connect(user='webapp', password='novovoom1web', host='db', database='NovoVoom')
    cursor = cnx.cursor(buffered=True)

    query = "INSERT into Employee (first, last, dept, phone) VALUES ('Matt', 'Lepinski', 'Software Development', '555-555-1234');"

    cursor.execute(query)

    cnx.commit()

    return "Successfully Inserted Matt Lepinski"

app.run(host='0.0.0.0', port=5000)
