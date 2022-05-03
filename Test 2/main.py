#knn
from tokenize import group
import numpy as np

#preparation for the data
def createDataSet():
    group = np.array([[1,101],[5,89],[108,5],[115,8]])
    labels = ['1','1','2','2']
    return group,labels

if __name__ == '__main__':
    group,labels = createDataSet()
    print(group)
    print(labels)
