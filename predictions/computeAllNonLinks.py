'''
Created on 2015年11月12日

@author: leo
'''

from tools.CommonTools import DataTools

def findAllNonlinks(allNodes, allLinks,*, storePath):
    nonlinks = []
    size = len(allNodes)
    with open(storePath, 'at') as storehandle: 
        for i in range(size):
            for j in range(i+1, size):
                link = '{0}-{1}\n'.format(allNodes[i], allNodes[j])
                if not link in allLinks:
                    storehandle.write(link)
                    nonlinks.append(link)
    return nonlinks




if __name__ == '__main__':
    import time
    tools = DataTools()
#     userpathes = ['youtube-users-part1.txt', 'youtube-users-part2.txt']
    allNodes, allTrainsLink = tools.loadData('formatedData')
    del allNodes
    allLinks = []
    for links in allTrainsLink.values():
        allLinks.extend(links)
    print('totoal links are : {0}'.format(len(allLinks)))
    with open('allTrainLinks', 'wt' , newline='\n') as storehandle:
        for link in allLinks:
            storehandle.write(link+"\n")
#     print('link: ', allLinks[0])
#     allNodes = []
#     start = time.clock()
#     for userpath in userpathes:
#         print('Begin collect users!')
#         for user in open(userpath, 'rt'):
#             allNodes.append(user)
#         print("Currently users are: ", len(allNodes))
#         print("Begin compute nonexisted links!")
# #         nonlinks = findAllNonlinks(allNodes, allLinks, storePath = 'nonlinks')
#         allNodes = []
#     
#     print("Cost time: {0}".format(time.clock() - start))
#     print('Total nonexisted links are: ', len(nonlinks))
#     print('Top 100 are: {0}'.format(nonlinks[0:101]))


            