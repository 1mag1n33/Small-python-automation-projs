from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='./templates', static_folder="./static")

@app.route('/')
def hello_world():
    return render_template('shh.html')