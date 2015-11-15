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
    NB = NaiveBayesModel()
    soce = NB.linkPredictionScore('869501', '869502', datatool.traindata_node_neighbors, allCC)
    