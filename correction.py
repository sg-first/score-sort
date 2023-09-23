import svd
import pickle
import numpy as np
import copy

def load(filename):
    f = open(filename, 'rb')
    return pickle.load(f)

centers = load('centers.pkl')

def getMidPos(pos1, pos2):
    midPos = []
    for i in range(len(pos1)):
        midPos.append((pos1[i] + pos2[i]) / 2)
    return midPos

midPos = getMidPos(centers[0], centers[1])

def cos(vec1,vec2):
    return float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))
allUserCos = {}

for id, vec in svd.denseUserVecs.data.items():
    cosVal = cos(vec, midPos)
    allUserCos[id] = cosVal

def test(k):
    dfData = copy.deepcopy(svd.dfData)

    rowNum = 1
    for row in dfData:
        for i in range(len(row.allScore)):
            id, oldScore = row.allScore[i]
            diff = k * allUserCos[id]
            newScore = oldScore + diff
            row.allScore[i] = (id, newScore)
        if rowNum == 23:
            break
        else:
            rowNum += 1

    rankDict = svd.getRankDict(dfData)
    return svd.calcRankDiff(rankDict)

minVal = 140
minK = None
for k in range(-1900, 0):
    v = test(k)
    if v < minVal:
        minVal = v
        minK = k
print(minVal, minK)