import networkx  as nx
from numpy.random import *
import matplotlib.pyplot as plt

#############################

G=nx.DiGraph()
for i in xrange(20):
    G.add_node(i,name=str(i))



for i in xrange(20):
    G.add_edge(randint(0,15),randint(0,15) )    
    
''''G.add_edge(1,2)
G.add_edge(1,5)
G.add_edge(5,2)
G.add_edge(3,2)  
G.add_edge(6,7)
G.add_edge(1,9) ''' 


nx.draw(G)
plt.show()