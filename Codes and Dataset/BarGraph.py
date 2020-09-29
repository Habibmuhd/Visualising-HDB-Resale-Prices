import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")

data = np.genfromtxt("resale-transactions-by-flat-type-based-on-registered-cases.csv", delimiter=',', skip_header=1, dtype=[("financial_year","i4"), ("flat_type","U10"), ("resale_transactions","i4")])
print("There are {} rows in this dataset".format(len(data)))

#extract rows with 5 rooms
keyword = "5 room"
column_to_search = data["flat_type"]
out = [i for i, v in enumerate(column_to_search) if keyword in v] #output = list with row numbers that match the condition
data_fiveroom = data[out] #data[row numbers] = actual data

#extract rows with 4 rooms
keyword = "4 room"
column_to_search = data["flat_type"]
out = [i for i, v in enumerate(column_to_search) if keyword in v] #output = list with row numbers that match the condition
data_fourroom = data[out] #data[row numbers] = actual data

ind = np.arange(len(data_fiveroom["flat_type"]))  # the x locations for the groups
width = 0.35  # the width of the bars
fig, ax = plt.subplots(1, figsize=(10,10))  #Creates just a figure and only one subplot

rects1 = ax.bar(ind - width/2, data_fiveroom["resale_transactions"], width, label='Five room transaction')
rects2 = ax.bar(ind + width/2, data_fourroom["resale_transactions"], width, label='Four room transaction')
labels = data_fiveroom['financial_year']


ax.set_ylabel('Number of Transaction')
ax.set_title('Number of resale transactions between 5 rooms HDB and 4 rooms HDB over the years')
ax.set_xticks(ind)
ax.set_xticklabels((labels))
ax.legend()



def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos]*3, 3),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom')


autolabel(rects1, "center")
autolabel(rects2, "center")

fig.tight_layout()

plt.show()