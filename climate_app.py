from flask import Flask, jsonify
import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import numpy as np

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)


#Flask set-up
app = flask(__name__)


#Flask Routes

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/temperature<br/>"
        f"/api/v1.0/ltstartdate&gt<br/>"
        f"/api/v1.0/ltenddate&gt<br/>"
        f"/api/v1.0/tobs<br/>"
    )

#List of API

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"Precipitation values:"
        f"/api/precipitation<br/>"
        f"Weather station list:"
        f"/api/stations<br/>"
        f"Temperature values:"
        f"/api/temperature<br/>"
       
    )


#APP Route- PRECIPITATION
@app.route("/api/precipitation")
def precipitation():
    """Return the JSON representation of the dictionary result from the query"""
  
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    last_date = dt.datetime.strptime(last_date[0], '%Y-%m-%d').date()
    one_year = last_date - dt.timedelta(days=365)
    
    results = session.query(Measurement.date,Measurement.prcp).\
    filter(Measurement.date >= one_year).all()

    dictreturn = dict(results)

    return jsonify(dictreturn)


#APP Route-Stations


@app.route("/api/stations")
def stations():
    """Return the JSON list of stations"""

    results = session.query(Station.name).all()
    
    return jsonify(results)


#APP Route- Temperature 

@app.route("/api/temperature")
def temperature():
    """Return the JSON representation of the dictionary result from the query"""
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    last_date = dt.datetime.strptime(last_date[0], '%Y-%m-%d').date()
    one_year = last_date - dt.timedelta(days=365)
    
    
    results = session.query(Measurement.tobs,Measurement.date).\
    filter(Measurement.date >= one_year).all()

    dictreturn = dict(results)

    return jsonify(dictreturn)