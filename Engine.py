from flask import Flask, render_template

Application = Flask(__name__)

@Application.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__": 
    Application.run(debug=True)