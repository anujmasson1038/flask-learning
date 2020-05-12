from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    #var_1 = {"Server-side": "Flask is server side scripting"}
    return "Flask is server side scripting"

app.run()
