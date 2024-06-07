from flask import Flask, render_template, request
import os, signal
import requests

url = "http://localhost:3000/push_attackP"

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
    file = open('DebugOut/nmap_all1.txt', 'w')
    file.write(data)
    file.close()
    os.system(f'python mulval_inp_gen.py DebugOut/nmap_all1.txt')

    File = open("DebugOut/attack.P", "r")
    Content = File.read()
    File.close()

    Response = requests.post(url, data=Content)

    File = open("static/assets/AG.pdf", "wb")
    File.write(Response.content)
    File.close()

    return {'Hello' : 'World'}
    

if __name__ == "__main__":
    app.run(debug=True, port=5000)