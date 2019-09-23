import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])
#a = a.apply(lambda n: float(n.replace(',','').replace('$','')))
a = a.str.replace(',','')
a = a.str.replace('$','')
a = a.astype(float)

print(a)
print(a.max())
print(a.min())

a_bins = pd.cut(a, [0,1250000, 2500000, 3750000, 5000000])
print(a_bins.value_counts())
#print(a_bins)
#print(a.value_counts(bins = 4))


hist_plot = a_bins.value_counts()

hist_plot.plot.hist( bins = 4)
plt.show()