# SQLAlchemy is good for establishing connections with less lines of code, based on psycopg2
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# This is address of the databse in the computer where the app is surreounding
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/pmc-app8'
psqldb = SQLAlchemy(app) # SQLAlchemy method to connect to db


# Model will be object Data, inherents from the Model class from the SQLAlchemy object
class Data(psqldb.Model):
    __tablename__='data'
    id=psqldb.Column(psqldb.Integer, primary_key=True)
    emai=psqldb.Column(psqldb.String(120))

# Map main homepage
@app.route("/")
def index():
    return render_template("index.html")

# Map success page
@app.route("/success", methods=['POST'])
def success():
    if(request.method == 'POST'):
        email = request.form['email_name'] # HTTP email request
        height = request.form['height_name'] # HTTP email request
        print(request.method)
        print(request.form) # ImmutableMultiDict([('email_name', 'EMAIL@gmail.com'), ('height_name', 'xxx.x')])
        print(email)
        print(height)
        return render_template("success.html")


if __name__  == "__main__":
    app.debug = True
    app.run() # or specify port app.run(port='5001')