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

@app.route("/Nessus", methods=['POST'])
def pNessus():
    data = request.json
    data = data['data']
    print(data)
    file = open('DebugOut/NessusXML.nessus', 'w')
    file.close()
    os.system(f'python attack_gen.py DebugOut/NessusXML.nessus')
    return {'data' : 'done'}


@app.route("/Nmap", methods=['POST'])
def pNmap():
    data = request.json
    data = data['data']
    print(data)
    file = open('DebugOut/nmap_all1.txt', 'w')
    file.close()
    os.system(f'python mulval_inp_gen.py DebugOut/nmap_all1.txt')
    return {'data' : 'done'}

if __name__ == "__main__":
    app.run()