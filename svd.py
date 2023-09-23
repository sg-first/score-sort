import pandas as pd
import numpy as np
import math
import copy

df = pd.read_excel('数据1.xlsx')

def newVec():
    return [0 for _ in range(2015)]

def newRankDict():
    ret = {}
    for i in range(1,24):  # 一共23个一等奖
        ret[i] = 0
    return ret

def calcRankDiff(rankDict):
    rankList = list(rankDict.items())
    rankList.sort(key=lambda x:x[1], reverse=True)
    print(rankList)
    nowRank = 1
    diffSum = 0
    for oldRank, _ in rankList:
        diff = math.fabs(nowRank - oldRank)
        # print(nowRank, oldRank, diff)
        diffSum += diff
        nowRank += 1
    return diffSum

allUserScore = {}
def addUserScore(id, score):
    if id not in allUserScore.keys():
        allUserScore[id] = []
    else:
        allUserScore[id].append(score)

def userScoreToAvg():
    for id, scoreList in allUserScore.items():
        s = sum(scoreList)
        avg = s / len(scoreList)
        allUserScore[id] = avg

class userVecs:
    def __init__(self, data = None):
        if data is None:
            self.data = {}
        else:
            self.data = data

    def addUserScore(self, id, score, index):
        if not pd.isna(id):
            addUserScore(id, score)
            if id not in self.data.keys():
                self.data[id] = newVec()
            self.data[id][index] = score

    def matToNewUserVecs(self, mat):
        newData = copy.copy(self.data)
        sub = 0
        for key in newData.keys():
            newData[key] = mat[sub]
            sub += 1
        return userVecs(newData)

    def toMat(self):
        sparseMat = []
        for id, vec in self.data.items():
            sparseMat.append(vec)
        sparseMat = np.array(sparseMat)
        return sparseMat

class dfRow:
    def __init__(self, rank):
        self.rank = rank
        self.allScore = []

    def addScore(self, id, score):
        if pd.isna(id):
            return False
        else:
            self.allScore.append((id, score))
            return True

    def getLastScore(self):
        sum = 0
        for id, score in self.allScore:
            sum += score
        return sum

sparseUserVecs = userVecs()
dfData = []

def getRankDict(dfData):
    rankDict = newRankDict()
    nowRank = 1
    for row in dfData:
        rankDict[nowRank] = row.getLastScore()
        nowRank += 1
    return rankDict

for index, row in df.iterrows():
    # if row['奖项'] == '一等奖':
    #     stdDict[int(row['名次'])] = row['专家一标准分（二）'] + row['专家二标准分（二）'] + row['专家三标准分（二）']
    sparseUserVecs.addUserScore(row['专家一编码'], row['专家一原始分'], index)
    sparseUserVecs.addUserScore(row['专家二编码'], row['专家二原始分'], index)
    sparseUserVecs.addUserScore(row['专家三编码'], row['专家三原始分'], index)
    sparseUserVecs.addUserScore(row['专家四编码'], row['专家四原始分'], index)
    sparseUserVecs.addUserScore(row['专家五编码'], row['专家五原始分'], index)
    sparseUserVecs.addUserScore(row['专家一编码（二）'], row['专家一原始分（二）'], index)
    sparseUserVecs.addUserScore(row['专家二编码（二）'], row['专家二原始分（二）'], index)
    sparseUserVecs.addUserScore(row['专家三编码（二）'], row['专家三原始分（二）'], index)
    # 收集所有二次评审分作为待修正数据
    rowData = dfRow(int(row['名次']))
    bSecondReview = True and rowData.addScore(row['专家一编码（二）'], row['专家一原始分（二）'])
    bSecondReview = bSecondReview and rowData.addScore(row['专家二编码（二）'], row['专家二原始分（二）'])
    bSecondReview = bSecondReview and rowData.addScore(row['专家三编码（二）'], row['专家三原始分（二）'])
    if bSecondReview:
        print(rowData.rank, rowData.allScore)
        dfData.append(rowData)

U, S, V = np.linalg.svd(sparseUserVecs.toMat())
denseUserVecs = sparseUserVecs.matToNewUserVecs(U)