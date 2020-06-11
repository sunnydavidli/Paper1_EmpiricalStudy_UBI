# change date and time of raw data
print("test!")
import datetime
import pandas as pd

print("change date and time of raw data")
dateColumns = ['event_time']
useCols = ['event_type', 'event_time', 'vehicle_id', 'total_mileage', 'event_lon', 'event_lat', 'speed']
df = pd.read_csv("./datasets/rawData.2017.11.01-2017.11.10.csv", sep=";", parse_dates=dateColumns, usecols=useCols)

print(df.head())
