'''Imports heap.'''
import heapq
class Node:
    '''Starts node.'''
    def __init__(self,f_y,symbol,l_t=None,r_t=None):
        #frequency of symbol
        self.freq=f_y
        #symbol name(character)
        self.symbol=symbol
        #node left of current node
        self.left=l_t
        #node right of current node
        self.right=r_t
        #tree direction(0/1)
        self.huff=' '
    def __lt__(self,nxt):
        return self.freq<nxt.freq
#utility function 
def print_nodes(node,val=''):
    '''Printz.'''
    newval=val+str(node.huff)
    if node.left:
        print_nodes(node.left,newval)
    if node.right:
        print_nodes(node.right,newval)
    if not node.left and not node.right:
        print_nodes(f"{node.symbol}->{newval}")

chars=['a','b','c','d','e','f']
freq=[5,9,12,13,16,45]
nodes=[]
for x in range(6):
    heapq.heappush(nodes,Node(freq[x],chars[x]))
while len(nodes)>1:
    left=heapq.heappop(nodes)
    right=heapq.heappop(nodes)

    left.huff=0
    right.huff=1

    newNode=Node(left.freq+right.freq,left.symbol+right.symbol,left,right)

    heapq.heappush(nodes,newNode)
print_nodes(nodes[0])
