'''
834. Sum of Distances in Tree
An undirected, connected tree with n nodes labelled 0...n-1 and n-1 edges are given.
The ith edge connects nodes edges[i][0] and edges[i][1] together.
Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.
Example 1:
Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation:
Here is a diagram of the given tree:
  0
 / \
1   2
   /|\
  3 4 5
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.
'''

class Node(object):
    def __init__(self,value):
        self.value = value
        self.child = []

class nArrryTree(object):
    def __init__(self,value):
        self.root = Node(value)

    def ComputeDistances(self):

        start = self.root
        output_lst = []

        nodes =[]
        nodes.append(start)
        nodes.append('NONE')
        height =0
        output_lst.append((start.value,0))
        height = height + 1

        while len(nodes)!=0:
            while nodes[0]!='NONE':
                tmp_node = nodes[0]
                nodes.pop(0)
                for item in tmp_node.child:
                    tup = (item.value,height)
                    output_lst.append(tup)
                    nodes.append(item)
            if nodes[0]=='NONE' and len(nodes)>1:
                nodes.pop(0)
                nodes.append('NONE')
                height = height +1
            else:
                nodes.pop()
                break

        print(output_lst)
        distances = 0
        for tup in output_lst:
            distances = distances + tup[1]
        print(distances)

def main():

    tree = nArrryTree(0)
    tree.root.child.append(Node(1))
    tree.root.child.append(Node(2))
    tree.root.child[1].child.append(Node(3))
    tree.root.child[1].child.append(Node(4))
    tree.root.child[1].child.append(Node(5))
    tree.ComputeDistances()

if __name__=='__main__':
    main()