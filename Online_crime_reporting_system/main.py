import os
import random
from datetime import date

#from nltk.stem import PorterStemmer
from urllib import request
import pymysql
import nltk
import smtplib, ssl
from flask import Flask, render_template, flash, request, session, current_app, send_from_directory, url_for
from werkzeug.utils import redirect, secure_filename

conn = pymysql.connect(user='root', password='', host='localhost', database='Online_crime')
port = 587
smtp_server = "smtp.gmail.com"
sender_email = "serverkey2018@gmail.com"
password ="extazee2018"

# UPLOAD_FOLDER = 'D:\\python\\Online_crime_reporting_system\\upload'
# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# UPLOAD_FOLD = 'D:\\python\\Online_crime_reporting_system\\upload'
# UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)

app = Flask(__name__, static_folder="static")
app.secret_key = 'abcdef'
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



################################################################### HOME
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user_login",methods=['GET','POST'])
def user_login():
    msg = ""

    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM user_register WHERE username = %s AND password = %s', (uname, pwd))
        account = cursor.fetchone()
        cursor.close()
        if account is None:
            msg = 'Incorrect username/password!'
            return render_template("user_login.html",msg=msg)
        else:
            session['uname'] = uname
            return redirect(url_for('user_home'))


        # Account doesnt exist or username/password incorrect
        # msg = 'Incorrect username/password!'
    return render_template("user_login.html")


@app.route("/user_register",methods=['GET','POST'])
def user_register():
    msg=""
    if request.method=='POST':
        name=request.form['name']
        mobileno=request.form['mobileno']
        email_address = request.form['mail_address']
        address=request.form['address']
        uname=request.form['username']
        password=request.form['password']
        today = date.today()
        rdate1 = today.strftime("%b-%d-%Y")
        mycursor = conn.cursor()
        mycursor.execute("SELECT max(id)+1 FROM user_register")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid = 1
        cursor = conn.cursor()
        sql = "INSERT INTO user_register(id,uname,mobile,email,address,username,password,rdate) VALUES ( %s, %s, %s, %s, %s, %s,%s,%s)"
        val = (maxid, name,  mobileno, email_address, address, uname, password,  rdate1)
        cursor.execute(sql, val)
        cursor.close()
        conn.commit()
        print(cursor.rowcount, "Registered Success")
        result = "sucess"

        if cursor.rowcount == 1:

            return redirect(url_for('user_login'))
        else:
            msg = "Could Not Be Stored..."
            return redirect(url_for('user_register'))
    else:

        render_template("user_register.html", msg=msg)
    return render_template("user_register.html")



@app.route("/user_home",methods=['GET','POST'])
def user_home():
    username = session['uname']
    return render_template("user_home.html",username=username)


@app.route("/complaints",methods=['GET','POST'])
def complaints():
    msg = ""
    uname = session['uname']
    if request.method == 'POST':
        name = request.form['name']
        reason = request.form['reason']
        address = request.form['address']
        status="Complaint"
        today = date.today()
        report=0
        rdate1 = today.strftime("%b-%d-%Y")
        mycursor = conn.cursor()
        mycursor.execute("SELECT max(id)+1 FROM complaint")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid = 1
        cursor = conn.cursor()
        sql1 = "INSERT INTO complaint(id,username,name,reason,address,status,report,cdate) VALUES ( %s,%s, %s, %s, %s, %s,%s,%s)"
        val = (maxid,uname, name, reason,  address, status, report,rdate1)
        cursor.execute(sql1, val)
        print (sql1)
        cursor.close()
        conn.commit()
        print(cursor.rowcount, "Complaint  Success")
        result = "sucess"
        if cursor.rowcount == 1:
            return redirect(url_for('view_complaint_status'))
        else:
            msg = "Could Not Be Stored..."
            return redirect(url_for('complaints'))
    else:

        render_template("complaint.html", msg=msg)
    return render_template("complaint.html")

@app.route("/crime_complaint",methods=['GET','POST'])
def crime_complaint():
    msg = ""
    username = session['uname']
    if request.method == 'POST':
        caddress = request.form['c_address']
        ctype = request.form['c_type']
        if 'file' not in request.files:
            flash('No file Part')
            return redirect(request.url)
        file = request.files['file']
        print(file)
        f = request.files['file']
        f.save(os.path.join("static/uploads/", secure_filename(f.filename)))
        status = "Complaint"
        today = date.today()
        rdate1 = today.strftime("%b-%d-%Y")
        mycursor = conn.cursor()
        mycursor.execute("SELECT max(id)+1 FROM crimes")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid = 1
        cursor = conn.cursor()
        report=0
        cursor.execute("insert into crimes values('"+str(maxid) + "','"+username +"','"+f.filename+"','"+ctype+"','"+caddress+"','"+status+"','"+str(report)+"','"+rdate1+"')")
        cursor.close()
        conn.commit()
        print(cursor.rowcount, "crimes  Success")
        result = "sucess"
        if cursor.rowcount == 1:
            return redirect(url_for('view_crimes_status'))
        else:
            msg = "Could Not Be Stored..."
            return redirect(url_for('crime_complaint'))
    else:

        render_template("crime.html", msg=msg)
    return render_template("crime.html")





@app.route("/missing_person",methods=['GET','POST'])
def missing_person():
    msg = ""
    username = session['uname']
    print(username)
    if request.method == 'POST':
        name = request.form['pname']
        age = request.form['age']
        gender = request.form['gender']
        mplace = request.form['m_place']
        mt = request.form['mt']
        mdate = request.form['m_date']
        if 'file' not in request.files:
            flash('No file Part')
            return redirect(request.url)
        file = request.files['file']
        print(file)
        f = request.files['file']
        f.save(os.path.join("static/uploads/", secure_filename(f.filename)))
        status = "Complaint"
        today = date.today()
        rdate1 = today.strftime("%b-%d-%Y")
        mycursor = conn.cursor()
        mycursor.execute("SELECT max(id)+1 FROM missing_person")
        maxid = mycursor.fetchone()[0]

        if maxid is None:
            maxid = 1
        cursor = conn.cursor()
        report=0
        cursor.execute("insert into missing_person values('"+str(maxid) + "','"+username +"','"+name +"','"+age +"','"+gender +"','"+mplace +"','"+mt +"','"+mdate +"','"+f.filename+"','"+status+"','"+str(report)+"','"+rdate1+"')")

        cursor.close()
        conn.commit()
        print(cursor.rowcount, "missing_person  Success")
        result = "sucess"
        if cursor.rowcount == 1:
            return redirect(url_for('view_missing_person_status'))
        else:
            msg = "Could Not Be Stored..."
            return redirect(url_for('missing_person'))
    else:

        render_template("missing_person.html", msg=msg)
    return render_template("missing_person.html")

@app.route("/view_status",methods=['GET','POST'])
def view_status():
    username = session['uname']
    conn1 = pymysql.connect("localhost", "root", "", "Online_crime")
    cursor = conn1.cursor()
    cursor.execute('SELECT * FROM  complaint WHERE username = %s', (username))
    account = cursor.fetchone()
    cursor.close()
    conn1.commit()
    return render_template("all_complaint_status.html",username=username,account=account)

@app.route("/view_complaint_status",methods=['GET','POST'])
def view_complaint_status():
    username = session['uname']
    conn1 = pymysql.connect("localhost", "root", "", "Online_crime")
    cursor = conn1.cursor()
    cursor.execute('SELECT * FROM  complaint WHERE username = %s', (username))
    items = cursor.fetchall()
    print(items)
    cursor.close()
    return render_template("view_complaint_status.html",username=username,items=items)

@app.route("/view_crimes_status",methods=['GET','POST'])
def view_crimes_status():
    username = session['uname']
    conn1 = pymysql.connect("localhost", "root", "", "Online_crime")
    cursor = conn1.cursor()
    cursor.execute('SELECT * FROM  complaint WHERE username = %s', (username))
    account = cursor.fetchall()
    cursor.close()
    return render_template("view_crimes_status.html",username=username,account=account)

@app.route("/view_missing_person_status",methods=['GET','POST'])
def view_missing_person_status():
    username = session['uname']
    conn1 = pymysql.connect("localhost", "root", "", "Online_crime")
    cursor = conn1.cursor()
    cursor.execute('SELECT * FROM  missing_person WHERE username = %s', (username))
    value = cursor.fetchall()
    print(value)
    cursor.close()
    return render_template("view_missing_person_status.html",username=username,value=value)


@app.route("/admin_login",methods=['GET','POST'])
def admin_login():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM admin WHERE username = %s AND password = %s', (uname, pwd))
        account = cursor.fetchone()
        cursor.close()
        if account is None:
            msg = 'Incorrect username/password!'
            return render_template("admin_login.html",msg=msg)
        else:
            session['uname'] = uname
            return redirect(url_for('admin_home'))


        # Account doesnt exist or username/password incorrect
        # msg = 'Incorrect username/password!'
    return render_template("admin_login.html")


@app.route("/admin_home",methods=['GET','POST'])
def admin_home():
    return render_template("admin_home.html")


@app.route("/admin_complaints",methods=['GET','POST'])
def admin_complaints():
    conn12 = pymysql.connect("localhost", "root", "", "Online_crime")
    cursor1 = conn12.cursor()
    cursor1.execute('SELECT * FROM  complaint')
    items = cursor1.fetchall()
    print(items)
    cursor1.close()
    return render_template("admin_complaints.html",items=items)

@app.route("/admin_crime_complaint",methods=['GET','POST'])
def admin_crime_complaint():
    conn13 = pymysql.connect("localhost", "root", "", "Online_crime")
    cursor2 = conn13.cursor()
    cursor2.execute('SELECT * FROM  crimes')
    val = cursor2.fetchall()
    conn13.commit()
    cursor2.close()

    return render_template("admin_crime_complaint.html",val=val)

@app.route("/admin_missing_person",methods=['GET','POST'])
def admin_missing_person():
    conn14 = pymysql.connect("localhost", "root", "", "Online_crime")
    cursor3 = conn14.cursor()
    cursor3.execute('SELECT * FROM  missing_person')
    account = cursor3.fetchall()

    cursor3.close()
    return render_template("admin_missing_person.html",account=account)




@app.route("/update_crime/<string:bid>",methods=['GET','POST'])
def update_crime(bid):
    print(bid)
    uid=""

    report=1
    status="Action Completed.."
    conn5 = pymysql.connect("localhost", "root", "", "Online_crime")
    cursor4 = conn5.cursor()
    sql = cursor4.execute('UPDATE  crimes SET status = %s, report=%s WHERE id=%s', (status,report, bid))
    print(sql)
    cursor4.close()
    conn5.commit()
    conn14 = pymysql.connect("localhost", "root", "", "Online_crime")
    cursor3 = conn14.cursor()
    cursor3.execute('SELECT * FROM  crimes')
    val = cursor3.fetchall()
    cursor3.close()
    return render_template("admin_crime_complaint.html",val=val)




@app.route("/update_complaint/<string:bid>",methods=['GET','POST'])
def update_complaint(bid):
    print(bid)
    status="Action Completed.."
    report=1
    conn5 = pymysql.connect("localhost", "root", "", "online_crime")
    cursor4 = conn5.cursor()
    sql = cursor4.execute('UPDATE  complaint SET status = %s, report=%s WHERE id=%s', (status, report,bid))
    cursor4.close()
    conn5.commit()
    conn14 = pymysql.connect("localhost", "root", "", "Online_crime")
    cursor3 = conn14.cursor()
    cursor3.execute('SELECT * FROM  complaint')
    items = cursor3.fetchall()
    cursor3.close()
    return render_template("admin_complaints.html",items=items)




@app.route("/update_missing/<string:bid>",methods=['GET','POST'])
def update_missing(bid):
    print(bid)
    status="Action Completed.."
    report=1
    conn5 = pymysql.connect("localhost", "root", "", "Online_crime")
    cursor4 = conn5.cursor()
    sql = cursor4.execute('UPDATE  missing_person SET status =%s,report=%s WHERE id=%s', (status,report, bid))
    cursor4.close()
    conn5.commit()
    conn14 = pymysql.connect("localhost", "root", "", "Online_crime")
    cursor3 = conn14.cursor()
    cursor3.execute('SELECT * FROM  missing_person')
    account = cursor3.fetchall()
    cursor3.close()
    return render_template("admin_missing_person.html",account=account)



##########################
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
