# -*- coding: utf-8 -*-P
"""
Created on Tue Jul  7 13:35:50 2020

@author: Devang Mehrotra
"""


from flask import Flask, request, render_template,redirect
import pandas as pd
import numpy as np
from flask_mysqldb import MySQL

app =Flask(__name__,template_folder='templates')


app.config['MYSQL_HOST'] = 'database'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ' '
#enter your mysql pwd
app.config['MYSQL_DB'] = 'db1'
app.config['MYSQL_PORT'] = 3308
mysql = MySQL(app)

day=None
feature=None

@app.route('/', methods=['GET', 'POST'])
def index():
    global day,feature
    if request.method == 'POST':
        day = request.form['day']
        feature = request.form['feature']
        if feature=="all":
            return redirect('/data1')
        else:
            return redirect('/data2')
    return render_template('index1.html')
    
@app.route('/data1')
def users():
    cur = mysql.connection.cursor()
    query="SELECT * FROM day{}".format(day)
    cur.execute(query)
    d1 = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('data1.html',c=d1)

@app.route('/data2')
def users1():
    cur = mysql.connection.cursor()
    query="SELECT {} FROM day{}".format(feature,day) 
    cur.execute(query)
    d1 = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('data2.html',c=d1,x=feature)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)

