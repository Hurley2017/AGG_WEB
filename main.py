from flask import Flask, render_template, request
import sys
from werkzeug.serving import make_server
import os, signal

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

    
@app.get('/shutdown')
def shutdown():
    sys.exit()

if __name__ == "__main__":
    app.run()