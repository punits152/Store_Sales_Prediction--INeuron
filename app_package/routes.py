from flask import render_template,redirect
from flask.helpers import url_for
from app_package import app
from app_package.forms import PredictionForm
import pickle
import numpy as np

with open("Model_and_analysis/regr_model",'rb') as f:
    estimator = pickle.load(f)

# All the routes of our application are here 
@app.route("/", methods=["GET","POST"])
@app.route("/home", methods=["GET","POST"])
def home_page():
    form = PredictionForm()
    if form.validate_on_submit() :
        X = np.array([[form.fat_regular.data,form.price.data,form.visibility.data,form.location_type_tier2.data,form.supermarket_type1.data,form.supermarket_type2.data,form.supermarket_type3.data]])
        y_hat = estimator.predict(X)[0]
        return render_template("result.html", y_hat=y_hat)
    
    elif form.errors != {}:
        for err_msg in form.errors.values():
            print(f"There wan an error with creating user: {err_msg}")
    
    return render_template("home_page.html",form=form)
    
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")