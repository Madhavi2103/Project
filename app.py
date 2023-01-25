from flask import Flask,flash,redirect,render_template,url_for,request,jsonify,session
from flaskext.mysql import MySQL
from flask_session import Session
from datetime import date
from datetime import datetime
import cryptography
import stripe
#from threading import Thread
#from secretconfig import secret_key
#from py_mail import mail_sender
import smtplib
stripe.api_key = "sk_test_51MMsHhSGj898WTbYXSx509gD14lhhXs8Hx8ipwegdytPB1Bkw0lJykMB0yGpCux95bdw1Gk9Gb9nJIWzPEEDxSqf00GEtCqZ8Y"
from email.message import EmailMessage
app=Flask(__name__)
app.secret_key='jr@547hhkghj'
app.config['MYSQL_DATABASE_HOST'] ='localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD']='Madhu-03'
app.config['MYSQL_DATABASE_DB']='BUS'
app.config['SESSION_TYPE']='filesystem'
mysql=MySQL(app)
Session(app)
@app.route('/')
def home():
    return render_template('index1.html')
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=="POST":
        print(request.form)
        user=request.form['user']
        cursor=mysql.get_db().cursor()
        cursor.execute('SELECT user_name from user')
        users=cursor.fetchall()
        password=request.form['password']
        cursor.execute('select password from user where user_name=%s',[user])
        data=cursor.fetchone()
        cursor.close()
        if (user,) in users:
            if password==data[0]:
                session['name']=user
                return redirect(url_for('home'))
            else:
                flash('Invalid Password')
                return render_template('login.html')
        else:
            flash('Invalid user id')
            flash('No account please singup')
            return render_template('login.html')      
    return render_template('login.html')        
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
        cursor.execute('insert ignore into user(user_name,email,mobile,password) values(%s,%s,%s,%s)',[user_name,email,mobile,password])
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
@app.route("/confirmed/<travels>",methods=['GET','POST'])
def confirm(travels):
    Name=session['name']
    if request.method=='POST':
        Date=request.form['d1']
        Timing=request.form['s11']
        Number=request.form['s7']
        Seats=request.form['s3']
        return redirect(url_for('pay',Name=Name,travels=travels,Date=Date,Timing=Timing,Number=Number,Seats=Seats))
    return render_template('book.html',title=travels,nam=Name)
@app.route('/pay/<Name>/<travels>/<Date>/<Timing>/<Number>/<Seats>',methods=['GET','POST'])
def pay(Name,travels,Date,Timing,Number,Seats):
    checkout_session=stripe.checkout.Session.create(
        success_url=request.host_url+url_for('success_pay',Name=Name,travels=travels,Date=Date,Timing=Timing,Number=Number,Seats=Seats),
        line_items=[
            {
                'price_data': {
                    'product_data': {
                        'name': f'{travels}\n{Date}\n{Timing}\ )',
                    },
                    'unit_amount': 487*100,
                    'currency': 'inr',
                },
                'quantity': Number,
            },
            ],
        mode="payment",)
    return redirect(checkout_session.url)
@app.route('/success/<Name>/<travels>/<Date>/<Timing>/<Number>/<Seats>')
def success_pay(Name,travels,Date,Timing,Number,Seats):
    cursor=mysql.get_db().cursor()
    cursor.execute("INSERT INTO booking(Name,travels,Date,Timings,Number,Seats) Values(%s,%s,%s,%s,%s,%s) " ,(Name,travels,Date,Timing,Number,Seats))
    mysql.get_db().commit()
    flash("Tickets Booked Successfully")
    return redirect(url_for('home'))
@app.route('/bookings')
def bookings():
    Name=session['name']
    cursor=mysql.get_db().cursor()
    cursor.execute('SELECT * from booking where name=%s',[gname])
    data=cursor.fetchall()
    return render_template('bookings.html',data=data)
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
app.run(debug=True)
















    
            

    
