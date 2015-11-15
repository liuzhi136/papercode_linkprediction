'''
Created on Nov 11, 2015

@author: leo
'''

import pickle

class DataTools:
    def __init__(self):
        #The total nodes in the data set of youtube
        self.allNodes = []
        #The total train data links(exclude test data) of youtube
        self.allTrainLinks = {}
        #A formated data that the format is node with its neighbors
        self.traindata_node_neighbors = {}
        #The test data that must be specified when formating training data
        self.testdata = []
        
    #formating the raw data set of youtube
    def formatData(self, *readPaths, storePath):
        #print('paths: {0}'.format(readPaths))
        try:
            i = 1
            for readpath in readPaths:
                if readpath == 'youtube-users.txt':
                    self.allNodes = [line.strip() for line in open(readpath, 'rt')]
                    continue
                key = 'train{0}'.format(i)
                with open(readpath, 'rt') as readhandle:
                    self.allTrainLinks[key] = [line.strip().replace('\t', '-') for line in readhandle if len(line) >= 2]
                i += 1
            print('end for loop: {0}'.format(i))
            with open(storePath, 'wb') as storehandle:
                pickle.dump(self.allNodes, storehandle)
                pickle.dump(self.allTrainLinks, storehandle)
        finally:
            print('this in format method!!')
            
    #this method is used to store the formated data. the order is nodes, links
    def loadData(self, storePath):
        try:
            with open(storePath, 'rb') as loadhandle:
                allNodes = pickle.load(loadhandle)
                allTrains = pickle.load(loadhandle)
                self.allTrainLinks = allTrains
                self.allNodes = allNodes 
        finally:
            print('This is in load method!')
        return allNodes,self.allTrainLinks
    
    #set the dict format train data into the {node:neighbors,...} and return test data and train data
    def getNode_neighbors(self, allTrains, testkey):
        self.testdata = [link.replace('\t', '-') for link in allTrains[testKey]]
        keys = list(allTrains.keys())
        keys.remove(testKey)
        for key in keys:
            traindata = allTrains[key]
            for link in traindata:
                nodes = link.split('-')
                #if the left node has been in the trainset, just append the right node into left's neighbor set or create a new node with its first neighbor
                if nodes[0] in self.traindata_node_neighbors:
                    self.traindata_node_neighbors[nodes[0]].append(nodes[1])
                else:
                    self.traindata_node_neighbors[nodes[0]] = [nodes[1]]
    
    def computeAllNodesCC(self, storeCCPath):
        allNodesCC = {}
        allLinks = []
        for links in self.allTrainLinks.values():
            allLinks.extend(links)
#         print('links: ', len(allLinks))
#         print('nodes: ', len(self.allNodes))
        for node in self.allNodes:
            neighbors = self.traindata_node_neighbors.get(node, None)
            count = 0
            if not neighbors: continue
            k = len(neighbors)
            for i in range(k):
                i_neighbors = self.traindata_node_neighbors.get(neighbors[i], None)
                if not i_neighbors: continue
                for j in range(i+1,k):
                    count += 1 if neighbors[j] in i_neighbors else 0
            CC = 2 * count / k * (k - 1)
#             print(node, ':', CC, '\tindex: ', index)
            allNodesCC[node] = CC
            
        with open(storeCCPath, 'wb') as cchandle:
            pickle.dump(allNodesCC, cchandle)   
        return allNodesCC



if __name__ == '__main__':
    import time
    tool = DataTools()
    #readpaths = ['youtube-users.txt', 'trainlink1-youtube', 'trainlink2-youtube', 'trainlink3-youtube','trainlink4-youtube', 'trainlink5-youtube', 'trainlink6-youtube', 'trainlink7-youtube', 'trainlink8-youtube', 'trainlink9-youtube', 'trainlink10-youtube']
    #print('begin to format......')
    #tool.formatData(*readpaths, storePath = 'formatedData')
    #print('-'*80)
    print('begin to load......')
    #allNodes, allTrains = tool.loadData('formatedData')
    testKey = 'train10'
    #tool.getNode_neighbors(allTrains, testKey)
    print('Get Node with its neighbors end......')
    print('Top 100 tested data are: {0}'.format(tool.testdata[0:101]))
    print('the total train links are : {0}'.format(len(tool.traindata_node_neighbors)))
    print('Begin to compute CC!')
    start = time.clock()
    #The stored order is that first is CC and second is NCCC
    #allNodesCC = tool.computeAllNodesCC('CC_NCCC')
    print('Costing time: {0}'.format(time.clock() - start))
    with open('CC_NCCC', 'rb') as cchandle:
        allNodesCC = pickle.load(cchandle)
    print('Computing node\'s CC totally are : ', len(allNodesCC))
    zeros = [zero for zero in allNodesCC.values() if zero == 0]
    i = 0
    print('The total CC contains {0} zero!'.format(len(zeros)))
    for n, cc in allNodesCC.items():
        if i == 100:break
        print(n, "->", cc)
        i += 1
    # print('allNodes: {0}, allTrains: {1}'.format(type(allNodes), type(allTrains)))
    # print('Total nodes are: {0}'.format(len(allNodes))) 
    # print('Top 100 nodes are : {0}'.format(allNodes[0:101]))
    # print('Total tains are : ' ,len(allTrains))
    # for (k,v) in allTrains.items():
    #     print(k, ' : ', v[0:101])
    # count = sum([len(v) for v in allTrains.values()])
    # print('Total links are: {0}'.format(count))