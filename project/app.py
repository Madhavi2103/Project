from flask import Flask,redirect,render_template,url_for,request,jsonify
from flaskext.mysql import MySQL
from datetime import date
from datetime import datetime
#from threading import Thread
#from secretconfig import secret_key
#from py_mail import mail_sender
import smtplib
from email.message import EmailMessage
app=Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] ='localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD']='Madhu-03'
app.config['MYSQL_DATABASE_DB']='BUS'
mysql=MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')
app.run(debug=True)
    
            

    
