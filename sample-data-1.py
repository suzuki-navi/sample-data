import random
import numpy as np


count = 100

def cluster(target, data1_av, data1_std, data2_av, data2_std, data3_av, data3_std):
    data1 = np.random.normal(data1_av, data1_std, count)
    data2 = np.random.normal(data2_av, data2_std, count)
    data3 = np.random.normal(data3_av, data3_std, count)

    result = []
    for i in range(count):
        result.append([target, data1[i], data2[i], data3[i]])
    return result

data1 = cluster(1, -2.0, 8.0, 1.0, 0.2, 0.3, 0.8)
data2 = cluster(2,  0.0, 5.0, 1.8, 0.2, 0.1, 0.5)
data3 = cluster(3,  1.0, 1.0, 1.7, 0.4, 1.6, 0.3)

data = data1 + data2 + data3
random.shuffle(data)

id = 1
for elem in data:
    print("{},{},{},{},{}".format(id, elem[0], elem[1], elem[2], elem[3]))
    id += 1

