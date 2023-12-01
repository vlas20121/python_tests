import pandas as pd
import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
headers = ['N','Date','Time','SensorValue']
#df = pd.read_csv('DataLog.CSV',parse_dates={"Datetime" : [1,2]},names=headers)
df = pd.read_csv('DataLog.CSV')
#,names=headers)
print (df)
plt.plot(df.N, df.SensorValue)
plt.show()

