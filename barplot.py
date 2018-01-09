import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("customs_revenue.csv")
data=data.as_matrix()


print(data[0,2:10])

import numpy as np


N = 8
revenue = data[0,2:10]/1000
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, revenue, width)

plt.ylabel('Customs revenue (in thousands of  crores rupees)')
plt.title('Customs Revenue of Machinery from 2006-2014')
plt.xticks(ind, ('2006-07', '2006-07', '2007-08', '2008-09', '2009-10','2010-11','2011-12','2012-13','2013-14'))
plt.yticks(np.arange(0, 80, 10))
plt.show()

