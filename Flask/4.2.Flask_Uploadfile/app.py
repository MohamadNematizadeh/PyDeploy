import os

from flask import Flask, request,session as flask_session, render_template, redirect, url_for
from pydantic import ValidationError
from ultralytics import YOLO
from PIL import Image

from model import LoginModel,RegisterModel
from data import Data

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads' 
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.secret_key = 'supersecretkey'

def allowed_file(file):
     return True
# Routes
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        password = data.get("password")
        confirmpassword = data.get("confirmpassword")

        if password != confirmpassword:
            return render_template('register.html', error='Passwords do not match')

        try:
            register_data = RegisterModel(
                first_name=data.get("first_name"),
                last_name=data.get("last_name"),
                email=data.get("email"),
                username=data.get("username"),
                age=data.get("age"),
                city=data.get("city"),
                country=data.get("country"),
                password=password
            )
        except ValidationError as e:
            return render_template('register.html', error=str(e))

        if Data.get_user_by_username(register_data.username):
            return render_template('register.html', error='Username already exists')
        
        Data.create_user(register_data)
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        try:
            login_data = LoginModel(username=data['username'], password=data['password'])
        except ValidationError as e:
            return render_template('login.html', error=str(e))

        user = Data.get_user_by_username(login_data.username)
        if not user or not Data.verify_password(login_data.password, user.password_hash):
            return render_template('login.html', error='Invalid credentials')

        return redirect(url_for("upload"))

    return render_template('login.html')


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == "GET":
        return render_template("upload.html")
    elif request.method == "POST":
        file = request.files['file']
        if file.filename == '':
            return redirect(url_for("upload"))
        else:
            
            if file and allowed_file(file.filename):
                save_pth = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
                file.save(save_pth)
                print(save_pth)
                model = YOLO("model/yolov8n-cls.pt")
                image = Image.open(save_pth)
                results = model(image) 
                result_image = results[0].plot() 
                for result in results:
                    print(result)  
                    results = result.names[result.probs.top1]

            return render_template("result.html",result=results)       

@app.route("/BMR",methods=['GET','POST'])
def  calculator_BMR():
    if request.method == "GET":
        return render_template("BMR_Calculator.html")
    elif request.method == "POST":
        gender = request.form["gender"]
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        age = float(request.form["age"])
        
        if gender == "Male":
            bmr =  66.5 + (13.75 * weight) + (5.003 * height) - (6.775 * age)
            print(bmr)

        elif gender == "Female":
            bmr =  655.1 + (9.563 * weight ) + (1.850 * height) - (4.676 * age)
            print(bmr)
        else:
            return "Invalid gender. Please select 'Male' or 'Female'."
        
        return render_template("bmr_result.html", bmr=bmr)

if __name__ == '__main__':
    app.run(debug=True)