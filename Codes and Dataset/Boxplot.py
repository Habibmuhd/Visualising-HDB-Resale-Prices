import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")
title = "Resale Price of flats in Singapore in Nov 2019"
data = np.genfromtxt("resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv", dtype=[("month","i4"),("town","U15"), ("flat_type","U10"), ("resale_price","i4")], delimiter= ",",  skip_header =60352, missing_values= ["na", "-", " "], filling_values=[0])

null_rows = np.isnan(data["resale_price"])
nonnull_values = data[null_rows == False]

labels = list(set(data["flat_type"])) #set all room types tgt
labels.sort()
print(labels)

levels = np.arange(0,len(labels))
levels_values = data[["flat_type", "resale_price"]]

values = levels_values["resale_price"]  #value of resale price

values_2rooms = values[levels_values["flat_type"] == "2 ROOM"]
values_3rooms = values[levels_values["flat_type"] == "3 ROOM"]
values_4rooms = values[levels_values["flat_type"] == "4 ROOM"]
values_5rooms = values[levels_values["flat_type"] == "5 ROOM"]
values_exe = values[levels_values["flat_type"] == "EXECUTIVE"]
values_mulgen = values[levels_values["flat_type"] == "MULTI-GENERATION"]

values_combined = [values_2rooms, values_3rooms, values_4rooms, values_5rooms, values_exe, values_mulgen]

print(len(values_combined)) #prints 6

plt.figure(2, figsize= (5,5)) # multiple box plots on one figure
plt.title(title, fontsize= 30 )
plt.ylabel("Resale Flat Price",fontsize = 10)
plt.yticks(fontsize = 10)
plt.xticks(fontsize = 10, rotation = "vertical")
bp_dict = plt.boxplot(values_combined,labels = labels, patch_artist= True)


#change outline color,
for box in bp_dict["boxes"]:
    box.set (color = "blue", linewidth= 2)
    box.set (facecolor= "green")

for whisker in bp_dict["whiskers"]:
    whisker.set (color= "black", linewidth= 2)

for cap in bp_dict["caps"]:
    cap.set (color= "black", linewidth= 2)

for median in bp_dict["medians"]:
    median.set (color= "blue", linewidth= 2)

for flier in bp_dict ["fliers"]:
    flier.set(marker= "D", color= "blue", alpha = 0.5)

print(bp_dict.keys())


for line in bp_dict['medians']:
    # get position data for median line
    x, y = line.get_xydata()[1] # top of median line
    # overlay median value
    plt.text(x, y, '%.1f' %y,horizontalalignment='center') # draw above, centered


fliers =[]
for line in bp_dict["fliers"]:
    ndarray = line.get_xydata()
    if (len(ndarray)>0):
        max_flier = ndarray[:,1].max()
        max_flier_index = ndarray[:,1].argmax()
        x = ndarray[max_flier_index,0]
        print("Flier: " + str(x) + "," + str(max_flier))
        plt.text(x,max_flier,"%.1f" % max_flier, horizontalalignment= 'center', fontsize = 10 ,color= "green")

plt.show()