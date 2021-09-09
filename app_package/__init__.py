from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET_KEY"]='187f4d4b72e4c031506a4ee2'

from app_package import routes
