'''
This problem was asked by Yelp.
The horizontal distance of a binary tree node describes how far left or right the node will be when the tree is printed out.
More rigorously, we can define it as follows:
The horizontal distance of the root is 0.
The horizontal distance of a left child is hd(parent) - 1.
The horizontal distance of a right child is hd(parent) + 1.
For example, for the following tree, hd(1) = -2, and hd(6) = 0.
             5
          /     \
        3         7
      /  \      /   \
    1     4    6     9
   /                /
  0                8
The bottom view of a tree, then, consists of the lowest node at each horizontal distance. If there are two nodes at the same depth and horizontal distance, either is acceptable.
For this tree, for example, the bottom view could be [0, 1, 3, 6, 8, 9].
Given the root to a binary tree, return its bottom view.
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

    def BottomViewTree(self):
        dict={}
        start=self.root
        node_lst=[]
        node_lst.append(start)
        node_lst.append('NONE')
        dict={}
        dict[start.value]=0
        vertical={}
        vertical[0]=[start.value]

        while len(node_lst)!=0:
            while node_lst[0]!='NONE':
                n=node_lst[0]
                node_lst.pop(0)
                if n.left!=None:
                    level=dict[n.value]
                    if level-1 in vertical.keys():
                        vertical[level-1].append(n.left.value)
                    else:
                        vertical[level-1]=[]
                        vertical[level-1].append(n.left.value)
                    dict[n.left.value]=level-1
                    node_lst.append(n.left)
                if n.right!=None:
                    level = dict[n.value]
                    if level + 1 in vertical.keys():
                        vertical[level + 1].append(n.right.value)
                    else:
                        vertical[level + 1] = []
                        vertical[level + 1].append(n.right.value)
                    dict[n.right.value] = level + 1
                    node_lst.append(n.right)
            if node_lst[0]=='NONE' and len(node_lst)==1:
                break
            else:
                node_lst.append('NONE')
                node_lst.pop(0)

        output_lst=[]
        for tup in sorted(vertical.items(),key=lambda x:x[0]):
            output_lst.append(tup[1][-1])
        return output_lst

def main():

    tree=BinaryTree(5)
    tree.root.left=Node(3)
    tree.root.right = Node(7)
    tree.root.left.left = Node(1)
    tree.root.left.right = Node(4)
    tree.root.left.left.left = Node(0)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(8)
    print(tree.PrintTree())
    print(tree.BottomViewTree())

if __name__=='__main__':
    main()