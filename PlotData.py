import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

dates = []
times = []
temps = []
y=[]
x=[]


with open("C:\\Programering\\python\\Uppgifter\\FileReadAndWrite\\smhi-opendata.csv","r",encoding="utf-8") as f:
    for line in f:
        lineData = line.split(";")
        dates.append(lineData[0])
        times.append(lineData[1])
        temps.append(lineData[2])
dataPoints = list(zip(dates,times,temps))


for data in dataPoints:
    dataAndTime = data[0] + " " + data[1]
    x.append(datetime.strptime(dataAndTime, "%Y-%m-%d %H:%M:%S"))
    y.append(float(data[2]))

plt.grid(True)
plt.plot(x,y)
plt.gcf().autofmt_xdate()
plt.show()


