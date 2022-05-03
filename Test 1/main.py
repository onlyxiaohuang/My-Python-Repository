import numpy as np
#from functools import reduce


def loadDataSet():#determine whether a sentense is offensive
    postingList=[]
    classVec=[]
    with open("text_for_positive.txt","r") as pos:
        for line in pos.readlines():
            line=line.strip('\n')
            postingList.append(line.split(' '))
            classVec.append(0)
    
    #print(postingList)

    with open("text_for_negative.txt","r") as neg:
        for line in neg.readlines():
            line=line.strip('\n')
            postingList.append(line.split(' '))
            classVec.append(1)#where offensive words' value are 1,otherwise 0
    

    return postingList,classVec

def createVocabList(dataSet):#Use set to get a table of distinct words
    vocabSet=set([])
    for document in dataSet:
        vocabSet=vocabSet|set(document)
    return list(vocabSet)

def setOfWord2Vec(vocabList,inputSet):#To get the vector
    returnVec=[0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]=1
        else: print("Error: the word: %s is not in my Vocabulary" %word)
    return returnVec

#preparation above

def trainNB0(trainMatrix,trainCategory):
    numTrainDocs=len(trainMatrix)
    numWords=len(trainMatrix[0])#count the sentense length
    pAbusive=sum(trainCategory)/float(numTrainDocs)
    p0Num=np.ones(numWords) 
    p1Num=np.ones(numWords)
    p0Denom=2.0
    p1Denom=2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num+=trainMatrix[i]#count the offensive P(wi|1)...
            p1Denom+=sum(trainMatrix[i])
        else:
            p0Num+=trainMatrix[i]
            p0Denom+=sum(trainMatrix[i])
    p1Vect=np.log(p1Num/p1Denom)
    p0Vect=np.log(p0Num/p0Denom)
    return p0Vect,p1Vect,pAbusive


def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):#determine whether these words are offensive
    p1=sum(vec2Classify*p1Vec)+np.log(pClass1)
    p0=sum(vec2Classify*p0Vec)+np.log(1.0-pClass1)
    print('p0:',p0)
    print('p1:',p1)
    if p1>p0:
        return 1
    else:
        return 0
 

def testingNB():#main part for testing a set of words
    listOPosts,listClasses=loadDataSet()
    myVocabList=createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWord2Vec(myVocabList,postinDoc))
    p0V,p1V,pAb=trainNB0(np.array(trainMat),np.array(listClasses))


    testEntry=['handsome','rich','happy']#asking whether they are offensive
    thisDoc=np.array(setOfWord2Vec(myVocabList,testEntry))
    if classifyNB(thisDoc,p0V,p1V,pAb):
        print(testEntry,'is offensive')
    else:
        print(testEntry,'is not offensive')

    testEntry=['stupid','pig',]
    thisDoc=np.array(setOfWord2Vec(myVocabList,testEntry))
    if(classifyNB(thisDoc,p0V,p1V,pAb)):
        print(testEntry,'is offensive')
    else:
        print(testEntry,'is not offensive')
    

if __name__ == '__main__':
    testingNB()


