"""
HISTOGRAM GRAPH PLOT CODE SAMPLE
HISTOGRAM PLOT FOR THE DATA HAS STRING CONTENT
FOR THE NUMERIC CONTENT PANDAS LIBRARY HAS BUILT-IN FUNCTIONS
"""

import matplotlib.pylab as plt
import pandas as pd
s1 = pd.Series(['a', 'b', 'a', 'c', 'a', 'b'])
s2 = pd.Series(['a', 'f', 'a', 'd', 'a', 'f', 'f'])
d = pd.DataFrame({'s1': s1, 's2': s2})
d.apply(pd.value_counts).plot(kind='bar', subplots=True)
plt.show()