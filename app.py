from flask import Flask,render_template,request
from project_1.db import Database
import project_1.api as api
app = Flask(__name__)

dbo = Database()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration', methods=['POST'])
# we need to specify the method as POST to handle form submissions
def perform_registration():
    name = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    responce = dbo.insert(username=name,email=email,password=password)
    if responce:
        return render_template('login.html' , message="Registration successful. Login to proceed")
    else:
        return render_template('register.html',message="Email already exists")

@app.route('/perform_login',methods=['POST'])
def perform_login():
    email = request.form.get("email")
    password = request.form.get("password")
    responce = dbo.search(email=email,password=password)

    if(responce):
        return "login successful"
    else:
        return render_template('login.html',message="PLEASE FILL CORRECT DETAILS")

@app.route('/profie')
def profile():
    return render_template("profile.html")

@app.route('/ner')
def ner():
    return render_template('ner.html')

@app.route('/perform_ner' , methods=['POST'])
def perform_ner():
    text = request.form.get("ner_text")
    responce = api.ner(text)
    return render_template ("ner.html",responce = responce)


app.run(debug=True)