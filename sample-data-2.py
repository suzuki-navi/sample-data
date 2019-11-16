import random
import numpy as np

def cluster(target, count, data1_av, data1_std, data2_av, data2_std):
    data1 = np.random.normal(data1_av, data1_std, count)
    data2 = np.random.normal(data2_av, data2_std, count)

    result = []
    for i in range(count):
        result.append([target, data1[i], data2[i]])
    return result


data1 = cluster(1, 100, 1.5, 0.1, 1.0, 0.1)
data2 = cluster(2, 100, 0.5, 0.3, 0.2, 0.4)
data3 = cluster(3,  90, 0.0, 3.0, 0.0, 3.0)
data4 = cluster(4,  10, 0.0, 9.0, 0.0, 9.0)

data = data1 + data2 + data3 + data4
random.shuffle(data)

id = 1
for elem in data:
    print("{},{},{},{}".format(id, elem[0], elem[1], elem[2]))
    id += 1

