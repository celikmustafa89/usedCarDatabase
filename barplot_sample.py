import matplotlib.pyplot as plt
import pandas as pd



colLabels=("Structure", "Energy", "Density")
nrows, ncols = len(clust_data)+1, len(colLables)
hcell, wcell = 0.3, 1.
hpad, wpad = 0, 0
fig=plt.figure(figsize=(ncols*wcell+wpad, nrows*hcell+hpad))
ax = fig.add_subplot(111)
ax.axis('off')
#do the table
the_table = ax.table(cellText=clust_data,
          colLabels=colLabels,
          loc='center')
plt.savefig("table.png")