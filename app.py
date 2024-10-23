from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/project",methods=["GET","POST"])
def loginform():
    if request.method =="POST":
        Name = (request.form["name"])
        Phoneno = (request.form["phoneno"])
        Email = (request.form["email"])
        return render_template("index.html",name=Name,phoneno=Phoneno,email=Email)
    else:
        return render_template("index.html") 