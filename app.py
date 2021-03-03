import os
import pandas as pd
import numpy as np

import sqlite3
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/bellybutton.sqlite"
print(os.environ.get('DATABASE_URL', ''))
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db/bellybutton.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/bellybutton.sqlite"
db = SQLAlchemy(app)


# reflect an existing database into a new model
Base = automap_base()
Base.prepare(db.engine, reflect=True)

# Save references to each table
Samples_Metadata = Base.classes.sample_metadata
Samples = Base.classes.samples

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

    @app.route("/names")
def names():
    """Return a list of sample names."""