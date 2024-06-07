from flask import Flask, request, send_file
import os

port = '3000'

 

Application = Flask(__name__)   

@Application.route("/push_attackP", methods=["GET","POST"])
def push_attackP():
    Data = request.data.decode("utf-8")
    File = open("Test.P", "w")
    File.write(str(Data))
    File.close()
    os.system("graph_gen.sh Test.P -v -p")
    return send_file("AttackGraph.pdf", as_attachment=True)





if __name__ == "__main__":
    Application.run(debug=True, port=port)