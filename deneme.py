# noinspection PyUnresolvedReferences

import numpy as np
import matplotlib.pyplot as plt


def createclustereddata(N, k):
    pointPerCluster = float(N) / k
    x = []
    y = []

    for i in range(k):
        incomeCentroid = np.random.uniform(20000.0, 200000.0)
        ageCentroid = np.random.uniform(20.0, 70.0)
        for j in range(int(pointPerCluster)):
            x.append([np.random.normal(incomeCentroid, 10000.0),
                      np.random.normal(ageCentroid, 2.0)])
            y.append(i)
    x = np.array(x)
    y = np.array(y)
    return x, y


(x, y) = createclustereddata(100, 5)
plt.figure(figsize=(8, 6))
plt.scatter(x[:, 0], x[:, 1], c=y.astype(np.float))
plt.show()
