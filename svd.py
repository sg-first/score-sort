import pandas as pd
import math

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

userVecs = {}

def addUserScore(id, score, index):
    if not pd.isna(id):
        if id not in userVecs.keys():
            userVecs[id] = newVec()
        userVecs[id][index] = score

for index, row in df.iterrows():
    # if row['奖项'] == '一等奖':
    #     stdDict[int(row['名次'])] = row['专家一标准分（二）'] + row['专家二标准分（二）'] + row['专家三标准分（二）']
    addUserScore(row['专家一编码'], row['专家一原始分'], index)
    addUserScore(row['专家二编码'], row['专家二原始分'], index)
    addUserScore(row['专家三编码'], row['专家三原始分'], index)
    addUserScore(row['专家四编码'], row['专家四原始分'], index)
    addUserScore(row['专家五编码'], row['专家五原始分'], index)
    addUserScore(row['专家一编码（二）'], row['专家一原始分（二）'], index)
    addUserScore(row['专家二编码（二）'], row['专家二原始分（二）'], index)
    addUserScore(row['专家三编码（二）'], row['专家三原始分（二）'], index)

for id, vec in userVecs.items():
    print(id, vec)
