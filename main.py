import pandas as pd
from matplotlib import pyplot as plt

sample=pd.read_csv('covid.csv')
print(sample)
type(sample)
plt.plot(sample.Monday )
plt.plot(sample.Tuesday)
plt.plot(sample.Wednesday)
plt.plot(sample.Thursday)
plt.plot(sample.Friday)
plt.plot(sample.Saturday)
plt.plot(sample.Sunday)
plt.legend(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])

plt.show()