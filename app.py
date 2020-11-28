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
# reference tables as classes 
Measurement = Base.classes.measurement
Station = Base.classes.station
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
# precipiation route    
@app.route("/api/v1.0/precipitation")
def precipitation():
    #data filter
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # build query
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    return jsonify(precipitation)

# station route     
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    # using np.ravel() to transform results into 1D array
    stations = list(np.ravel(results))
    # assigning the string "station" to be equal to the station results
    return jsonify(stations=stations)

#temperature observation route
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


