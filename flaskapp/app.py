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

@app.route("/our_services/assessment/")
def our_services_assessment():
    """function to render the assessment.html template"""
    return render_template("assessment.html")

@app.route("/our_services/preparation/")
def our_services_preparation():
    """function to render the preparation.html template"""
    return render_template("preparation.html")

@app.route("/our_services/demolition/")
def our_services_demolition():
    """function to render the demolition.html template"""
    return render_template("demolition.html")

@app.route("/our_services/repair/")
def our_services_repair():
    """function to render the repair.html template"""
    return render_template("repair.html")

@app.route("/our_services/recreation/")
def our_services_recreation():
    """function to render the recreation.html template"""
    return render_template("recreation.html")

@app.route("/our_services/specialty_services/")
def our_services_specialty_services():
    """function to render the specialty_services.html template"""
    return render_template("specialty_services.html")

@app.route("/our_markets/")
def our_markets():
    """function to render the our_markets.html template"""
    return render_template("our_markets.html")

@app.route("/our_markets/commercial/")
def our_markets_commercial():
    """function to render the commercial.html template"""
    return render_template("commercial.html")

@app.route("/our_markets/education_centers/")
def our_markets_education_centers():
    """function to render the education_centers.html template"""
    return render_template("education_centers.html")

@app.route("/our_markets/fitness_facilities/")
def our_markets_fitness_facilities():
    """function to render the fitness_facilities.html template"""
    return render_template("fitness_facilities.html")

@app.route("/our_markets/healthcare/")
def our_markets_healthcare():
    """function to render the healthcare.html template"""
    return render_template("healthcare.html")

@app.route("/our_markets/office/")
def our_markets_office():
    """function to render the office.html template"""
    return render_template("office.html")

@app.route("/our_markets/retail/")
def our_markets_retail():
    """function to render the retail.html template"""
    return render_template("retail.html")

