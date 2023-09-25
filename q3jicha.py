import pandas as pd
import matplotlib.pylab as plt

df = pd.read_csv('极差.csv')

jicha = []
for index, row in df.iterrows():
    if row['一阶段成绩1']>41.638 and row['一阶段成绩1']<58.3136:
        jicha.append(row['极差1'])

plt.hist(jicha, bins=20)
plt.show()