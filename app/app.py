import os
from flask import Flask, render_template, request, flash, redirect
from flask_assets import Environment
from webassets import loaders
import boto3



app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config['DEBUG'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = False
app.config['SECRET_KEY'] = "123"

# asset pipeline
assets = Environment(app)
#bundles = loaders.YAMLLoader('./static/js/js-assets.yml').load_bundles()
#[assets.register(name, bundle) for name, bundle in bundles.items()]
##bundles = loaders.YAMLLoader('./static/styles/css-assets.yml').load_bundles()
#[assets.register(name, bundle) for name, bundle in bundles.items()]


@app.route("/")
def index():
    return "Welcome to jDubs App 4"



if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=80)