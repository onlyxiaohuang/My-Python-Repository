#knn
#from tokenize import group
import numpy as np
import operator

#preparation for the data
def createDataSet():
    group = np.array([[1,101],[5,89],[108,5],[115,8]])
    labels = ['1','1','2','2']
    return group,labels


def classify0(inX,dataSet,labels,k):
    #shape[0] means the rows
    dataSetSize = dataSet.shape[0]
    #repeat the array
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet

    #count the differences between two vectors
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndices = distances.argsort()


    #count the apperances of each label
    classCount = {}
    for i in range (k) :
        voteIlabel = labels[sortedDistIndices[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    
    #itemgetter was used for sorting
    #reverse means sorting from big to small ones
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse = True)

    return sortedClassCount[0][0]

if __name__ == '__main__':
    group, labels = createDataSet()
    test = [101,20]
    #k = 3 
    test_class = classify0(test, group, labels, 3)
    print(test_class)


'''
if __name__ == '__main__':
    group,labels = createDataSet()
    print(group)
    print(labels)
'''