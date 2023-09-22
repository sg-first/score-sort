allC = []

for id in range(1, 121):
    c = set()
    for offset in range(5):
        c.add(id + offset)
    allC.append(c)

# 补上以121-125开头的循环的情况
for id in range(121, 126):
    c = set()
    for offset in range(5):
        val = id + offset
        if val > 125:
            val -= 125
        c.add(val)
    allC.append(c)

def getCNum(id):
    num = 0
    coopId = []
    for c in allC:
        if id in c:
            print(c)
            coopId += list(c)
            num += 1
    print(set(coopId))
    return num

getCNum(3)

def getCNumTot(ids):
    num = 0
    for id in ids:
        num += getCNum(id)
    return num

