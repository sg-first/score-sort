import svd
import pickle
import numpy as np

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

k = 54.8721 / 0.0489

rowNum = 1
for row in svd.dfData:
    for i in range(len(row.allScore)):
        id, oldScore = row.allScore[i]
        print(k * allUserCos[id])
        newScore = oldScore + k * allUserCos[id]
        row.allScore[i] = (id, newScore)
    if rowNum == 23:
        break
    else:
        rowNum += 1

rankDict = svd.getRankDict(svd.dfData)
print(svd.calcRankDiff(rankDict))