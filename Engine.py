from flask import Flask

Application = Flask(__name__)

@Application.route("/")
def home():
    return "Hello, World!"

if __name__ == "__main__": 
    Application.run()