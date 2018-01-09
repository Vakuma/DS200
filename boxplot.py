

import numpy

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data=pd.read_csv("customs_revenue.csv")
data=data.as_matrix()




# don't show outlier points
plt.figure()
plt.boxplot(np.transpose(data[11:16,2:10]/100), 0,'')
plt.title('Plot of revenue(in hundreds of crores of rupees) for various metals')

plt.show()