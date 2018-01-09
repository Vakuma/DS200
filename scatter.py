import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("customs_revenue.csv")
data=data.as_matrix()


print(data[0,2:10])

import numpy as np


N = 8
revenue_electrical_machinery = data[2,2:10]/1000
revenue_fruits = data[31,2:10]/1000

print(revenue_fruits)
ind = np.arange(8)*0.251

colors = np.random.rand(2)
p1 = plt.scatter(revenue_fruits, revenue_electrical_machinery, c=['r'], alpha=0.5)

plt.ylabel('Customs revenue of eletrical machinery(in thousands of crore rupees)')
plt.xlabel('Customs Revenue of Fruits(in thousands of crore rupees)')
plt.title('Customs Revenue of Eletrical machinery versus fruits  from 2006 to 2014')
#plt.yticks(np.arange(0, 80, 10))
plt.show()





# x = np.arange(0.0, 50.0, 2.0)
# y = x ** 1.3 + np.random.rand(*x.shape) * 30.0
# s = np.random.rand(*x.shape) * 800 + 500

# plt.scatter(x, y, s, c="g", alpha=0.5, marker=r'$\clubsuit$',
#             label="Luck")
# plt.xlabel("Leprechauns")
# plt.ylabel("Gold")
# plt.legend(loc=2)
# plt.show()
