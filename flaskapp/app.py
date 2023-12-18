from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    """function to render the index.html template"""
    return render_template("index.html")