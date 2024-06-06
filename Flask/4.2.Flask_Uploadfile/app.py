import os
from deepface import DeepFace
from flask import Flask,render_template,request,redirect,session,url_for

app = Flask("Face Analyez")
app.config['UPLOAD_FOLDER'] = 'uploads'  # Update with your upload folder path
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(file):
     return True

def auth(email,password):
    if email == "mohmmad@game.com.mohmmad" and password == "1234":
        return True
    else:
        return False    

@app.route("/")
def input():
    return render_template("index.html")

@app.route("/login" ,methods=['GET','POST'])
def login():
    if request.method =="GET":
        return render_template("login.html")
    elif request.method=="POST":
        emaile = request.form["email"]
        password = request.form["password"]
        result = auth(emaile,password)
        if result :
            return redirect(url_for("upload"))
        else:
            return redirect(url_for("login"))
            
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
                result = DeepFace.analyze(img_path = save_pth,actions = ['age']) 

            return render_template("result.html",result=result)       



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
if __name__ == "__main__":
    app.run(debug=True)        