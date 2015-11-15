'''
Created on 2015年11月12日

@author: leo
'''

class NaiveBayesModel:
    
    def __init__(self, *, v , e):
        self.len_V = v
        self.len_E = e
        self.len_U = self.len_V * (self.len_V - 1) // 2
        self.nodes_NCCC = {}


    def linkPredictionScore(self, x, y, nodes_neighbors, allNodesCC):
        xnei = nodes_neighbors.get(x,  None)
        ynei = nodes_neighbors.get(y, None)
        if not xnei or not ynei: return 0;
        sx = set(xnei)
        sy = set(ynei)
        #compute the intersection of x and y
        s_xy = sx & sy
        intersection_xy = list(s_xy)
        size = len(intersection_xy)
        coefficient = (self.len_U / self.len_E - 1) ** (size - 1)
        socre_xy = 1.0
        for node in intersection_xy:
            n_nei = nodes_neighbors.get(node, None)
            if not n_nei: continue
            node_neighbor = set(n_nei)
            #C(node) = F(x) & F(y) & F(node) U (x,y)
            Cn = node_neighbor & s_xy | {x, y}
            node_NCCC = self.compute_NCCC(Cn, node_neighbor, nodes_neighbors, allNodesCC)
            #store the NCCC of the given node to use it conveniently.
            self.nodes_NCCC[node] = node_NCCC
            print(node, '->', node_NCCC)
            socre_xy *= (node_NCCC/(1-node_NCCC))
        socre_xy *= coefficient
        return socre_xy
    
    #compute a node's NCCC
    def compute_NCCC(self, Cn, node_neighbor, nodes_neighbors, allNodesCC):
        denominator = numerator = 0.0
        for i in Cn:
            i_nei = nodes_neighbors.get(i, 0)
            if i_nei == 0: continue
            i_degree = len(i_nei)
            i_cc = allNodesCC.get(i, 0)
            numerator += (1/i_degree + i_cc)
        for j in node_neighbor:
            j_nei = nodes_neighbors.get(j, 0)
            if j_nei == 0: continue
            j_degree = len(j_nei)
            if j_degree == 0: continue
            j_cc = allNodesCC.get(j, 0)
            denominator += (1/j_degree + j_cc)
        return numerator / denominator
        