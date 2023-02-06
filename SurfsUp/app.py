# Import required libraries and dependencies
import pandas as pd
import numpy as np
import datetime as dt
import sqlalchemy
from flask import Flask, jsonify
from datetime import date, timedelta
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

# Create an engine for the SQLite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect the existing database into a new model
Base = automap_base()

# Reflect the tables in the database
Base.prepare(engine, reflect=True)

# Save references to the measurement and station tables
measurement = Base.classes.measurement
station = Base.classes.station

# Initialize a Flask app
app = Flask(__name__)

# Define the home route
@app.route("/")
def home():
    # Return a message with a list of available API routes
    return (
        f"<h1> Welcome to the Hawaii Climate API!</h1>"
        f"<h2><bold>Available routes:</bold></h2>"
        f"<b>Precipitation</b>:        /api/v1.0/precipitation<br/>"
        f"<b>List of Stations</b>:     /api/v1.0/stations<br/>"
        f"<b>Temp at the Most Active Station for 1 Year </b>:    /api/v1.0/tobs<br/><br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )

# Define the precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    # Query the date column of the Measurement table for the most recent date
    recent_date = session.query(measurement.date).order_by(measurement.date.desc()).first()
    
    # Convert the most recent date string to a date object
    recent_date = dt.date(2017,8,23) - dt.timedelta(days=365)
    
    # Calculate the date one year prior to the most recent date
    year_ago = recent_date - dt.timedelta(days=365)
    
    # Query the date and prcp columns of the Measurement table for data from the past year
    precipitation = session.query(measurement.date, measurement.prcp).\
        filter(measurement.date >= year_ago).\
        order_by(measurement.date).all()
    
    # Convert the query results to a dictionary
    precipitation_dict = {date: prcp for date, prcp in precipitation}
    
    # Return the dictionary as JSON data
    return jsonify(precipitation_dict)

# Define the station route
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    # Query the station table to retrieve the name and station columns
    result = session.query(station.name, station.station).all()
    
    # Convert the result of the query into a list of dictionaries
    stations = [{"name": row[0], "station": row[1]} for row in result]
    
    # Return the list of dictionaries as a JSON object
    return jsonify(stations)

# Define the tobs route
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    # Query the most active station from the measurement table
    most_active_station = session.query(measurement.station, func.count(measurement.station)).\
                                  group_by(measurement.station).\
                                  order_by(func.count(measurement.station).desc()).first()[0]
    # Find the most recent date for the most active station
    recent_date = session.query(measurement.date).\
                            filter(measurement.station == most_active_station).\
                            order_by(measurement.date.desc()).first()[0]
    # Calculate the date one year prior to the recent date
    one_year_ago = dt.datetime.strptime(recent_date, '%Y-%m-%d') - dt.timedelta(days=365)
    # Query tobs data for the previous year from the most active station
    tobs_data = session.query(measurement.date, measurement.tobs).\
                           filter(measurement.date >= one_year_ago).\
                           filter(measurement.station == most_active_station).\
                           order_by(measurement.date).all()
    # Convert the tobs query results to a dictionary and return it as JSON
    tobs_list = []
    for date, tobs in tobs_data:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        tobs_list.append(tobs_dict)
    return jsonify(tobs_list)

# Define Start date temperature route
@app.route("/api/v1.0/<start>")
def start_date(start):
    session = Session(engine)
    # Query for TMIN, TAVG, and TMAX for the given start date
    result = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).filter(measurement.date >= start).all()
    # Convert the query results to a dictionary and return as JSON
    start_data = {"TMIN": result[0][0], "TAVG": result[0][1], "TMAX": result[0][2]}
    return jsonify(start_data)

# Define Start and end date temperature route
@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    session = Session(engine)
    # Query for TMIN, TAVG, and TMAX between start and end dates
    result = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).filter(measurement.date >= start).filter(measurement.date <= end).all()
    # Convert the query results to a dictionary and return as JSON
    start_end_data = {"TMIN": result[0][0], "TAVG": result[0][1], "TMAX": result[0][2]}
    return jsonify(start_end_data)

# Check if the file is being executed as the main program, and run the application in debug mode if it is
if __name__ == "__main__":
    app.run(debug=True)