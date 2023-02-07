# sql-challenge
# BootCamp - Module 10 Challenge
Student Name - Anush De Costa Module 10 Challenge Name - SurfsUp SQLAlchemy-Challenge

## Introduction

This project is focused on analyzing the climate data from Honolulu, Hawaii and creating a Flask API based on the analysis. The data used in this project is obtained from the Hawaii climate data, which is stored in a sqlite database.  and includes information about precipitation and temperature observations for various weather stations in Honolulu. The data analysis is performed using Python and SQLAlchemy, and the Flask API is designed to provide a simple interface for accessing the analyzed data.

## Data Analysis

The data analysis is performed using Python and SQLAlchemy and involves the following steps:

* Connecting to the Hawaii climate database using the SQLAlchemy create_engine() function
* Reflecting the database tables into classes using the SQLAlchemy automap_base() function
* Creating a SQLAlchemy session to link Python to the database
* Performing a precipitation analysis
    * Finding the most recent date in the dataset
    * Querying the previous 12 months of precipitation data
    * Loading the query results into a Pandas DataFrame
    * Plotting the results using the DataFrame plot method
    * Printing summary statistics for the precipitation data
* Performing a station analysis
    * Calculating the total number of stations in the dataset
    * Finding the most-active stations
    * Calculating the lowest, highest, and average temperatures for the most-active station
    * Querying the previous 12 months of temperature observation (TOBS) data for the most-active station
    * Plotting the results as a histogram
* Closing the SQLAlchemy session

## Flask API

The Flask API is designed to provide a simple interface for accessing the analyzed climate data. The API includes the following routes:

* /: Start at the homepage and list all the available routes
* /api/v1.0/precipitation: Return the JSON representation of the precipitation data for the previous year
* /api/v1.0/stations: Return a JSON list of all the weather stations in the dataset
* /api/v1.0/tobs: Return a JSON list of temperature observations for the previous year for the most-active station
* /api/v1.0/<start> and /api/v1.0/<start>/<end>: Return a JSON list of the minimum temperature, average temperature, and maximum temperature for a specified start or start-end range

## Tools
* Jupyter Notebook
* VSCode
* SQLAlchemy
* Pandas
* Matplotlib
* Python 
* Flask

## Files

* Data Analysis - 
    * [Climate Analysis](./SurfsUp/climate_Final.ipynb)

* Data Analysis - 
    * [Climate Flask App](./SurfsUp/app.py)