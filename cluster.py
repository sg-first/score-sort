import svd
from sklearn.cluster import KMeans
import matplotlib.pylab as plt
import numpy as np
from scipy.stats import ttest_ind
import pickle

def save(filename, obj):
    f = open(filename, 'wb')
    pickle.dump(obj, f)
    f.close()

save('denseUserVecs.pkl', svd.denseUserVecs)

def cluster(infered_vectors_list, n_clusters):
    kmean_model = KMeans(n_clusters=n_clusters)
    kmean_model.fit(infered_vectors_list)
    # labels = kmean_model.predict(infered_vectors_list[0:100])
    return kmean_model.labels_ , kmean_model.cluster_centers_

labels, centers = cluster(svd.U, 2)
print(labels)
save('centers.pkl', svd.denseUserVecs)

# 将labels转换到对应专家
userList = list(svd.sparseUserVecs.data.keys())
userToLabelMap = {}
for i in range(len(labels)):
    userToLabelMap[userList[i]] = labels[i]
print(userToLabelMap)
save('userToLabelMap.pkl', userList)

# 两类专家平均分画图
svd.userScoreToAvg()
list1 = []
list0 = []
for id in userList:
    if userToLabelMap[id] == 1:
        list1.append(svd.allUserScore[id])
    else:
        list0.append(svd.allUserScore[id])

print(max(list1), min(list1), np.mean(list1))
print(max(list0), min(list0), np.mean(list0))
t_statistic, p_value = ttest_ind(list1, list0)
print(p_value)

plt.bar(range(len(list1)), list1)
plt.show()
plt.bar(range(len(list0)), list0)
plt.show()