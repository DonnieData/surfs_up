# import dependencies 
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#access SQLite database 
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect database 
Base = automap_base()
Base.prepare(engine, reflect=True)
# create session 
session = Session(engine)

# Set Up Flask
app = Flask(__name__)
#create Flask Routes 
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')