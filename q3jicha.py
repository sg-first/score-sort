import pandas as pd
import matplotlib.pylab as plt

df = pd.read_csv('极差.csv')
plt.hist(df['极差2'], bins=20)
plt.show()