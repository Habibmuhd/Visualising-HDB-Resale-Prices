import numpy as np
import matplotlib.pyplot as plt


plt.style.use("ggplot")

d = np.genfromtxt("land-area-and-dwelling-units-by-town.csv", delimiter=',', skip_header=242, skip_footer=1, dtype=[("financial_year","i4"),("town","U18"),("total_land_area","i4"),("residential_land_area","i4"),("dwelling_units_under_management","i4"), ("projected_ultimate_dwelling_units","i4")])
print("There are {} rows in this dataset".format(len(d)))

x = d["total_land_area"]
y = d["dwelling_units_under_management"]
z = d["town"]
h = d["residential_land_area"]  #residential_land_area"


print(z)

plt.scatter(h,y,)
plt.title("Number of units vs Residential Land area in 2018 (Density)", fontsize=18, y=1.03)
plt.xlabel('Residential land area (hectares)')
plt.ylabel('Dwelling units under management')

for i, txt in enumerate(z):   #label each plot
    plt.annotate(txt, (h[i], y[i]), horizontalalignment='right', verticalalignment='bottom', xytext=(45, -20), textcoords='offset pixels',)


plt.legend()
plt.show()