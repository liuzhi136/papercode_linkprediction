'''
Created on 2015年11月15日

@author: leo
'''

from NaiveBayesModel import  NaiveBayesModel
from CommonTools import  DataTools
from readfileRandom import readline
import random
import pickle

if __name__ == '__main__':
    datatool = DataTools()
    allNodes, allTrainLinks = datatool.loadData('formatedData')
    datatool.getNode_neighbors(allTrainLinks, "train10")
    allCC = datatool.loadCC('CC_NCCC')
    NB = NaiveBayesModel(v = len(allNodes), e = len(allTrainLinks))
    numnonlinks = 137623363
    readnum = 4538
    testlink= datatool.testdata
    #print('before: ', len(testlink), 'one of its\' element is ', testlink[0] )
    print('begin to select test link!')
    for i in range(0, readnum):
        randIndex = int(random.uniform(1, numnonlinks))
        line = readline('nonlinks', randIndex)
        print(line)
        testlink.append(line.strip())
    print('selelct test link finished!')
    predictRes = {}
    for line in testlink:
        if '-' in line:
            nodes = line.split('-')
            score = NB.linkPredictionScore(nodes[0], nodes[1], datatool.traindata_node_neighbors, allCC)
            print('the score of {0} and {1} is: {2}'.format(nodes[0], nodes[1],score))
            predictRes[line] = score
    with open('predictiveRes', 'wb') as handle:
        pickle.dump(predictRes, handle)
