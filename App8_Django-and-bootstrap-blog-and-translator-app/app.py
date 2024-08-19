# HOSTED AT: https://devconstructor.pythonanywhere.com/

# SQLAlchemy is good for establishing connections with less lines of code, based on psycopg2
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sendEmail import sendEmail
from sqlalchemy.sql import func
from werkzeug.utils import secure_filename
import io, csv


# INSTANTIATE YOUR POSTGRES DB AND THEN RUN THIS WITH (python):
    # from app import app, psqldb
    ## Creating an application context
    # with app.app_context():
    #     # Now you can safely call methods that require the application context
    #     psqldb.create_all()
    #     print("Database tables created.")



app = Flask(__name__)
# This is address of the database in the computer where the app is surrounding
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/pmc-app8'
psqldb = SQLAlchemy(app) # SQLAlchemy method to connect to db


# Model will be object Data, inherits from the Model class from the SQLAlchemy object
class Data(psqldb.Model):
    __tablename__ = 'data'
    id = psqldb.Column(psqldb.Integer, primary_key=True)
    email = psqldb.Column(psqldb.String(120), unique=True)
    height = psqldb.Column(psqldb.Float)
    
    def __init__(self, email_, height_):
        self.email = email_
        self.height = height_

# Map main homepage
@app.route("/")
def index():
    return render_template("index.html")

# Map success page
@app.route("/success", methods=['POST'])
def success():
    if(request.method == 'POST'):
        if('file' in request.files):
            file = request.files['file']
        if file.filename != '':
            # content = file.read()
            # print(content)
            # print("\n", file)
            # file.seek(0)
            # file.save("uploaded_files/" + secure_filename("uploaded_" + file.filename)) # uploads secure file for download
            # return render_template("success.html")
            
            # Check if the file is a CSV
            if not file.filename.lower().endswith('.csv'):
                return render_template("index.html",
                                text="Only CSV files are allowed!")
            
            checkRepeated= False
            stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None) # Stream file
            csv_input = csv.reader(stream)
            next(csv_input) # Skip the header titles row
            
            for row in csv_input:
                email = row[0]
                print("EMAIL FOR ROW: " + email)
                height = row[1]
                print("HEIGHT FOR ROW: " + height)
                print("COUNT OF EXISTING FOR EMAIL: " + str(psqldb.session.query(Data).filter(Data.email == email).count()))
                if psqldb.session.query(Data).filter(Data.email == email).count() == 0:
                    print(email, height)
                    data = Data(email, height)
                    psqldb.session.add(data)
                    psqldb.session.commit()
                    averageHeight = psqldb.session.query(func.avg(Data.height)).scalar()
                    averageHeight = round(averageHeight, 1)
                    submissionCount = psqldb.session.query(Data.height).count()
                    sendEmail(email, height, averageHeight, submissionCount)
                else:
                    checkRepeated = True
            
            if(checkRepeated == False):
                return render_template("success.html")
            
            else:
                # return render_template("success.html", tex)
                return render_template("success.html", 
                                       text="One or more of your files has already been inputted before.<br>------------<br> However, it has been omitted during this upload.<br>------------<br> Thank you! ")
        else:
            email = request.form['email_name'].strip().lower() # HTTP email request
            height = request.form['height_name'] # HTTP email request
            # print(request.method)
            # print(request.form) # ImmutableMultiDict([('email_name', 'EMAIL@gmail.com'), ('height_name', 'xxx.x')])
            # print(email, height, (psqldb.session.query(Data).filter(Data.email == email).count() == 0))
            if(psqldb.session.query(Data).filter(Data.email == email).count() == 0): # Will ony add to db if email is unique
                data = Data(email, height)
                psqldb.session.add(data)
                psqldb.session.commit()
                averageHeight = psqldb.session.query(func.avg(Data.height)).scalar()
                averageHeight = round(averageHeight, 1)
                submissionCount = psqldb.session.query(Data.height).count()
                sendEmail(email, height, averageHeight, submissionCount)
                return render_template("success.html")
    return render_template("index.html",
                           text="Seems like we've got something from that email address already!")


if __name__  == "__main__":
    app.debug = False # Turn off when deployment
    app.run() # or specify port app.run(port='5001')