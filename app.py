from flask import Flask,flash,redirect,render_template,url_for,request,jsonify
from flaskext.mysql import MySQL
from datetime import date
from datetime import datetime
import cryptography
#from threading import Thread
#from secretconfig import secret_key
#from py_mail import mail_sender
import smtplib
from email.message import EmailMessage
app=Flask(__name__)
app.secret_key='jhj'
app.config['MYSQL_DATABASE_HOST'] ='localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD']='Madhu-03'
app.config['MYSQL_DATABASE_DB']='BUS'
mysql=MySQL(app)

@app.route('/')
def home():
    return render_template('index1.html')
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        return render_template('login.html')
        user=request.form['user_name']
        password=request.form['password']
        cursor=mysql.get_db().cursor()
        cursor.execute('SELECT user_name,password from user where user_name=%s password=%s',[user_name,password])
        data=cursor.fetchall()[0]
        userid=data[0]
        admin_password=data[1]
        cursor.close()
        return redirect(url_for('home'))
    return render_template('login.html')
    '''if user_name==user_name and password==password:
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))'''
        #return redirect(url_for('index'))
@app.route('/index1',methods=['GET','POST'])
def home1():
    return render_template('index1.html')
@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        print(request.form)
        user_name=request.form['user_name']
        email=request.form['email']
        mobile=request.form['mobile']
        password=request.form['password']
        #conn=mysql.connect()
        cursor=mysql.get_db().cursor()
        cursor.execute('insert into user(user_name,email,mobile,password) values(%s,%s,%s,%s)',[user_name,email,mobile,password])
        mysql.get_db().commit()
        cursor.close()
        return redirect(url_for('login'))
    return render_template('signup.html')
@app.route('/logout')
def logout():
    return render_template('logout.html')
@app.route('/index1')
def index1():
    return render_template('index1.html')
@app.route('/classify',methods=['POST'])
def choose():
    print(request.form)
    choice1=request.form['option1']
    choice2=request.form['option2']
    if choice1=='Vijayawada' and choice2=='Hyderabad':
         return redirect(url_for('vijhyd'))
    elif choice1=='Vijayawada' and choice2=='Guntur':
        return redirect(url_for('vijgun'))
    elif choice1=='Vijayawada' and choice2=='Ongole':
        return redirect(url_for('vijong'))
    elif choice1=='Vijayawada' and choice2=='Tenali':
        return redirect(url_for('vijten'))
    elif choice1=='Guntur' and choice2=='Vijayawada':
        return redirect(url_for('vijgun'))
    elif choice1=='Hyderabad' and choice2=='Vijayawada':
        return redirect(url_for('vijhyd'))
    elif choice1=='Ongole' and choice2=='Vijayawada':
        return redirect(url_for('vijong'))
    elif choice1=='Tenali' and choice2=='Vijayawada':
        return redirect(url_for('vijten'))
    elif choice1=='Guntur' and choice2=='Hyderabad':
        return redirect(url_for('gunhyd'))
    elif choice1=='Hyderabad' and choice2=='Guntur':
        return redirect(url_for('gunhyd'))
    elif choice1=='Guntur' and choice2=='Ongole':
        return redirect(url_for('gunong'))
    elif choice1=='Ongole' and choice2=='Guntur':
        return redirect(url_for('gunong'))
    elif choice1=='Guntur' and choice2=='Tenali':
        return redirect(url_for('gunten'))
    elif choice1=='Tenali' and choice2=='Guntur':
        return redirect(url_for('gunten'))
    elif choice1=='Hyderabad' and choice2=='Ongole':
        return redirect(url_for('hydong'))
    elif choice1=='Ongole' and choice2=='Hyderabad':
        return redirect(url_for('hydong'))
    elif choice1=='Tenali' and choice2=='Hyderabad':
        return redirect(url_for('tenhyd'))
    elif choice1=='Hyderabad' and choice2=='Tenali':
        return redirect(url_for('tenhyd'))
    elif choice1=='Tenali' and choice2=='Ongole':
        return redirect(url_for('tenong'))
    elif choice1=='Ongole' and choice2=='Tenali':
        return redirect(url_for('tenong'))
@app.route('/home(1)')
def vijhyd():
    return render_template('home(1).html')
@app.route('/cards1')
def vijgun():
    return render_template('cards1.html')
@app.route('/cards2')
def vijong():
    return render_template('cards2.html')
@app.route('/cards3')
def vijten():
    return render_template('cards3.html')
@app.route('/cards4')
def gunhyd():
    return render_template('cards4.html')
@app.route('/cards5')
def gunong():
    return render_template('cards5.html')
@app.route('/cards6')
def gunten():
    return render_template('cards6.html')
@app.route('/cards7')
def hydong():
    return render_template('cards7.html')
@app.route('/cards8')
def tenhyd():
    return render_template('cards8.html')
@app.route('/cards9')
def tenong():
    return render_template('cards9.html')
@app.route('/index')
def index():
    return render_template('index.html')
'''@app.route('/passenger',methods=['GET','POST'])
def passenger():
    if request.method=='POST':
        #pass_id=request.form['pass_id']
        pass_name=request.form['pass_name']
        mobile=request.form['mobile']
        age=request.form['age']
        gender=request.form['gender']
        cursor=mysql.get_db().cursor()
        cursor.execute('insert into passenger(pass_name,mobile,age,gender) values(%s,%s,%s,%s)', [pass_name,mobile,age,gender])
        mysql.get_db().commit()
        cursor.close()
        return render_template('passenger.html')'''
@app.route('/payment',methods=['GET','POST'])
def payment():
    return render_template('payment.html')
@app.route('/ticket',methods=['GET','POST'])
def ticket():
    return render_template('ticket.html')
app.run(debug=True)
















    
            

    
