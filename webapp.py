from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/getvisitors")
def nice():
    return json.dumps({"Typ":"Mensch", "Anzahl": 13, "Alter": 4}) 

if __name__ == '__main__':
    app.run(host='0.0.0.0')
