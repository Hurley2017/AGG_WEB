from flask import Flask, render_template, request
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
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server shutting down...'

if __name__ == "__main__": 
    app.run()