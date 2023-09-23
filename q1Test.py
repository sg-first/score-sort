import matplotlib.pylab as plt
import numpy as np
import random

allC = []
selectNum = {}
for i in range(1, 126):
    selectNum[i] = 0

def randC():
    c = set()
    while len(c) < 5:
        id = random.randint(1, 125)
        c.add(id)
        selectNum[id] += 1
    return c

for _ in range(3000):
    allC.append(randC())

def calcTotIntersect(sub):
    ids = allC[sub]
    num = 0
    for otherIds in allC:
        num += len(otherIds & ids)
    return num - 5

intNums = []
for i in range(3000):
    intNums.append(calcTotIntersect(i))

print('平均数', np.mean(intNums))
print('中位数', np.median(intNums))
print('极差', max(intNums) - min(intNums))

plt.ylim(60, 160)
plt.bar(selectNum.keys(), selectNum.values())
plt.show()
plt.hist(intNums, bins=80)
plt.show()