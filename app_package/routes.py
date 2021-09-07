from flask.templating import render_template
from app_package import app

# All the routes of our application are here
@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home_page.html")