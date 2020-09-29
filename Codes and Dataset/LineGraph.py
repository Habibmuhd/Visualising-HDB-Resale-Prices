import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn-dark-palette")
data = np.genfromtxt("number-of-mrt-and-lrt-stations.csv", delimiter=',', skip_header=1, skip_footer= 1, dtype=[("year","i4"), ("mrt","i4")])
print("There are {} rows in this dataset".format(len(data)))

data2 = np.genfromtxt("public-transport-journeys.csv", delimiter=',', skip_header=1, dtype=[("year","i4"), ("average_daily_passenger_journeys","i4")])
print("There are {} rows in this dataset".format(len(data2)))



fig, ax = plt.subplots(1, figsize=(10,10))  #Creates just a figure and only one subplot

color = 'tab:red'
ax.plot(data["year"], data["mrt"], color= color, label= "MRT stations", linestyle= "--" )
ax.set_xlabel("Years") #set the x-axis name
ax.set_ylabel("Number of Mrt Stations",color = color) #set the yaxis name
ax.tick_params(axis='y', labelcolor=color)

ax1 = ax.twinx() #instantiate a second axes that shares the same x-axis
ax1.set_ylabel('Number of Passengers (Daily)', color='blue') # already handled the x-label with ax
ax1.plot(data2["year"], data2["average_daily_passenger_journeys"], label= "Number of Passengers")
ax1.tick_params(axis='y', labelcolor="blue")

ax.set_title('Number of Mrt Stations vs Ridership over the years',fontsize=18, y=1.03)
fig.tight_layout() #otherwise the right y-label is slightly clipped
plt.legend(loc="upper left")
plt.show()


