'''
Created on 2015年11月15日

@author: leo
'''

from tools.NaiveBayesModel import  NaiveBayesModel
from tools.CommonTools import  DataTools

if __name__ == '__main__':
    datatool = DataTools()
    allNodes, allTrainLinks = datatool.loadData('formatedData')
    datatool.getNode_neighbors(allTrainLinks, "train10")
    allCC = datatool.loadCC('CC_NCCC')
    NB = NaiveBayesModel(v = len(allNodes), e = len(allTrainLinks))
    score = NB.linkPredictionScore('1', '23', datatool.traindata_node_neighbors, allCC)
    print('the score of ', '1 and ', '23 is : ', score)
    