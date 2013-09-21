from flask import Flask
from parser import extensionDoc
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world"

@app.route("/getDoc")
def getDoc():
    doc = extensionDoc()
    json_formate = doc.downLoadDoc()
    return json_formate

if __name__ == "__main__":
    app.run()

