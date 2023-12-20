from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    """function to render the index.html template"""
    return render_template("index.html")

@app.route("/contact_us/")
def contact():
    """function to render the contact.html template"""
    return render_template("contact.html")

@app.route("/our_story/")
def our_story():
    """function to render the our_story.html template"""
    return render_template("our_story.html")

@app.route("/our_services/")
def our_services():
    """function to render the our_services.html template"""
    return render_template("our_services.html")

@app.route("/our_markets/")
def our_markets():
    """function to render the our_markets.html template"""
    return render_template("our_markets.html")