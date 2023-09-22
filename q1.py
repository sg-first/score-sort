allC = []

def gen(k):
    for id in range(1, 126):
        c = set()
        for offset in range(5):
            val = id + offset + k
            if val > 125:
                val -= 125
            c.add(val)
        allC.append(c)

for k in range(24):
    gen(k)

print('num:', len(allC))

def getCNum(id):
    num = 0
    coopId = []
    for c in allC:
        if id in c:
            # print(c)
            coopId += list(c)
            num += 1
    # print(set(coopId))
    return num

def getCNumTot(ids):
    num = 0
    for id in ids:
        num += getCNum(id)
    return num

def calcTotIntersect(sub):
    ids = allC[sub]
    num = 0
    for otherIds in allC:
        num += len(otherIds & ids)
    return num - 5

print(calcTotIntersect(0))
print(calcTotIntersect(49))