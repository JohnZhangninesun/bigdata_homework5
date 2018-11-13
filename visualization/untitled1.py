# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 08:37:42 2018

@author: 张旭
"""
import matplotlib.pyplot as plt

clusterNum = input("输入初始节点数:")
fileName = "clusternum" + clusterNum
f = open(fileName, "r")
lines = f.readlines()
f.close()
clusters = []
x = []
y = []

for line in lines:
    splitVec = line.split("	")
    clusters.append(int(splitVec[0]))
    z=splitVec[1].split(",")
    x.append(float(z[0]))
    y.append(float(z[1]))

plt.scatter(x, y, c=clusters, marker='o')
plt.title("KMeans cluster=" + clusterNum)
plt.savefig(fileName + ".png")
plt.show()