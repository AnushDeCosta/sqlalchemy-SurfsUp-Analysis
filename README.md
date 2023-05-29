# Surf's Up!: Hawaiian Climate Examination and Flask API Deployment

![Surf copy](https://github.com/AnushDeCosta/sqlalchemy-SurfsUp-Analysis/assets/67308030/2039dab7-2e58-4d82-b6c7-ad75e6b6439a)

## Introduction
This Analysis is set out to investigate climate patterns in Honolulu, Hawaii, and design a Flask API, furnishing easy access to the processed climate data. The investigation centers around precipitation and temperature records gathered from various weather stations in Honolulu, archived in a SQLite database. The analysis was executed using Python and SQLAlchemy, with the Flask API serving as an efficient gateway for data retrieval.

## Probing Climate Data
Climate data analysis was orchestrated using Python and SQLAlchemy, following a sequence of steps:
1. **Establishing Database Connection:** Leveraged SQLAlchemy's create_engine() function to form a connection with the Hawaiian climate database.
2. **Reflecting Database Structure:** Utilized SQLAlchemy's automap_base() function to mirror the database tables into classes, creating an effective representation.
3. **Initiating Database Session:** Forged a SQLAlchemy session to bridge the Python environment with the database.
4. **Precipitation Analysis:** Began with identifying the most recent date in the dataset, proceeding with a query for the past 12 months' precipitation data. The data was then imported into a Pandas DataFrame, plotted, and summary statistics were produced.
5. **Station Analysis:** This involved the calculation of the total number of stations, identification of the most active stations, and computation of the lowest, highest, and average temperatures for the most active station. Further, temperature observation data (TOBS) from the past 12 months for the most active station was queried and visualized as a histogram.
6. **Session Termination:** The SQLAlchemy session was carefully closed upon completion of tasks.

## Flask API
The Flask API was crafted to provide a streamlined interface to access the analyzed climate data. The API comes with the following routes:
- '/': Starts with the homepage and enumerates all available routes.
- '/api/v1.0/precipitation': Returns a JSON representation of the past year's precipitation data.
- '/api/v1.0/stations': Offers a JSON list of all weather stations in the dataset.
- '/api/v1.0/tobs': Provides a JSON list of temperature observations from the past year for the most active station.
- '/api/v1.0/' and '/api/v1.0/': Generates a JSON list of minimum, average, and maximum temperatures for a specified start or start-end range.

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
