'''
987. Vertical Order Traversal of a Binary Tree
Given a binary tree, return the vertical order traversal of its nodes values.
For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).
Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes,
we report the values of the nodes in order from top to bottom (decreasing Y coordinates).
If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.
Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.
Example 1:
Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).
Example 2:
Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,value):
        self.root=Node(value)

    def Preorder(self,start,tmp):
        if start is None:
            return
        tmp.append(str(start.value))
        self.Preorder(start.left,tmp)
        self.Preorder(start.right,tmp)

    def PrintTree(self):
        start=self.root
        tmp=[]
        self.Preorder(start,tmp)
        return '-'.join(tmp)

    def VerticalOrderTraversal(self):
        output_lst=[]
        start=self.root
        node_lst=[]
        node_lst.append(start)
        node_lst.append('NONE')
        element_dict={}
        vertical_dict={}
        vertical_dict[0]=[]
        vertical_dict[0].append(start.value)
        element_dict[start.value]=0

        while len(node_lst)!=0:
            while node_lst[0]!="NONE":
                n=node_lst[0]
                node_lst.pop(0)
                if n.left!=None:
                    val=element_dict[n.value]
                    if val-1 in vertical_dict.keys():
                        vertical_dict[val-1].append(n.left.value)
                    else:
                        vertical_dict[val-1]=[]
                        vertical_dict[val-1].append(n.left.value)
                    element_dict[n.left.value]=val-1
                    node_lst.append(n.left)
                if n.right != None:
                    val = element_dict[n.value]
                    if val + 1 in vertical_dict.keys():
                        vertical_dict[val + 1].append(n.right.value)
                    else:
                        vertical_dict[val + 1] = []
                        vertical_dict[val + 1].append(n.right.value)
                    element_dict[n.right.value] = val + 1
                    node_lst.append(n.right)
            if len(node_lst)==1 and node_lst[0]=='NONE':
                break
            else:
                node_lst.pop(0)
                node_lst.append('NONE')
        for tup in sorted(vertical_dict.items(),key=lambda x:x[0]):
            output_lst.append(tup[1].copy())
        return output_lst

def main():

    tree=BinaryTree(3)
    tree.root.left=Node(9)
    tree.root.right = Node(20)
    tree.root.right.left = Node(15)
    tree.root.right.right = Node(7)
    print(tree.PrintTree())
    print(tree.VerticalOrderTraversal())

    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    print(tree.PrintTree())
    print(tree.VerticalOrderTraversal())

if __name__=='__main__':
    main()