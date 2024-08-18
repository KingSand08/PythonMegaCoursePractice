from flask import Flask, render_template, request

app = Flask(__name__)

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