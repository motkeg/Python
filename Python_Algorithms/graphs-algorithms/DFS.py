import networkx  as nx
import matplotlib.pyplot as plt

import cProfile ,pstats

class TestDfs(object):
    
    def __init__(self):
        
        self.nodes = []
        self.graph = nx.DiGraph()
        self.Adj = {}

    def test_dfs(self):
        
        for id in range(0, 6):
            self.nodes.append(self.graph.add_node(id,name=str(id)))
        self.graph.add_edge(0, 1,  weight=5)
        self.graph.add_edge(0, 4, weight=3)
        self.graph.add_edge(0, 5, weight=2)
        self.graph.add_edge(1, 3, weight=5)
        self.graph.add_edge(1, 4, weight=4)
        self.graph.add_edge(2, 1, weight=6)
        self.graph.add_edge(3, 2, weight=7)
        self.graph.add_edge(3, 4, weight=8)
        
        self.Adj=self.BuildAdj()
        
        #nx.draw(self.graph)     #
        #plt.show()              # Uncomment to see visual graph
        self.dfs()
        self.bfs()
        
    def BuildAdj(self):
        list={}
        temp=[]
        for i in self.graph.nodes():
            temp=[]
            for j in self.graph.nodes():
                if (i,j) in self.graph.edges() and i!=j:
                    temp.append(j)
            list[i]=temp
        return list    
                
    def getAdj(self,node,reverse=False):
            
            if reverse == True:        
                return sorted(self.Adj[node], reverse=True)         
            return self.Adj[node]       
        
    def dfs(self):
                 
        visit, stack = [],[0]
        while (stack):
            v=stack.pop()
            if(v not in visit):
                visit.append(v)
                for u in self.getAdj(v,True):
                    stack.append(u)        
               
        print "DFS result:", visit       
    
    
    def bfs(self):
        L ,visit=[0] ,[]
        while L:
            v=L[0]
            if(v not in visit):
                visit.append(v)
                for u in self.getAdj(v):
                    if u not in visit:
                        L.append(u)
            L = L[1:]
        print "BFS result:", visit
                   
        
 

def Main():
    test = TestDfs()
    test.test_dfs()


if __name__ == '__main__':
   cProfile.run('Main()','log.txt')   
   p = pstats.Stats('log.txt')
   p.strip_dirs().sort_stats('calls').print_stats()