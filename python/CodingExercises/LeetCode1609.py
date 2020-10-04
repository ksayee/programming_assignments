'''
A binary tree is named Even-Odd if it meets the following conditions:
The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.
Example 1:
Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
Output: true
Explanation: The node values on each level are:
Level 0: [1]
Level 1: [10,4]
Level 2: [3,7,9]
Level 3: [12,8,6,2]
Since levels 0 and 2 are all odd and increasing, and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.
Example 2:
Input: root = [5,4,2,3,3,7]
Output: false
Explanation: The node values on each level are:
Level 0: [5]
Level 1: [4,2]
Level 2: [3,3,7]
Node values in the level 2 must be in strictly increasing order, so the tree is not Even-Odd.
Example 3:
Input: root = [5,9,1,3,5,7]
Output: false
Explanation: Node values in the level 1 should be even integers.
Example 4:
Input: root = [1]
Output: true
Example 5:
Input: root = [11,8,6,1,3,9,11,30,20,18,16,12,10,4,2,17]
Output: true
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class BinaryTree(object):
    def __init__(self,value):
        self.root=Node(value)

    def PreOrder(self,start,tmp):

        if start is None:
            return
        tmp.append(str(start.value))
        self.PreOrder(start.left,tmp)
        self.PreOrder(start.right,tmp)

    def PrintTree(self):
        start=self.root
        tmp=[]
        self.PreOrder(start,tmp)
        return '-'.join(tmp)

    def GetLevelOrderTraversal(self):

        start=self.root
        node_lst=[]
        dict={}
        height=0
        dict[height]=[]
        dict[height].append(start.value)
        node_lst.append(start)
        node_lst.append('NONE')
        tmp=[]

        while len(node_lst)!=0:
            while node_lst[0]!='NONE':
                node=node_lst[0]
                node_lst.pop(0)
                if node.left is not None:
                    tmp.append(node.left.value)
                    node_lst.append(node.left)
                if node.right is not None:
                    tmp.append(node.right.value)
                    node_lst.append(node.right)

            if node_lst[0]=='NONE' and len(node_lst)==1:
                node_lst.pop(0)
                break
            else:
                height=height+1
                dict[height]=tmp.copy()
                tmp=[]
                node_lst.pop(0)
                node_lst.append('NONE')
        return dict

    def EvenOddTree(self,dict):
        print(dict)

        flg=False

        sort_dict=sorted(dict.items(),key=lambda x:x[0])

        for tup in sort_dict:
            if tup[0]%2!=0:
                lst=[]
                for item in tup[1]:
                    if item%2==0:
                        if len(lst)==0:
                            lst.append(item)
                        elif lst[-1]>item:
                            lst.append(item)
                        else:
                            return False
                    else:
                        return False
            elif tup[0]%2==0:
                lst=[]
                for item in tup[1]:
                    if item%2!=0:
                        if len(lst)==0:
                            lst.append(item)
                        elif lst[-1]<item:
                            lst.append(item)
                        else:
                            return False
                    else:
                        return False

        return True

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(10)
    tree.root.right = Node(4)
    tree.root.left.left=Node(3)
    tree.root.right.left=Node(7)
    tree.root.right.right=Node(9)
    tree.root.left.left.left=Node(12)
    tree.root.left.left.right=Node(8)
    tree.root.right.left.left=Node(6)
    tree.root.right.right.right=Node(2)
    print(tree.PrintTree())
    dict=tree.GetLevelOrderTraversal()
    print(tree.EvenOddTree(dict))

    tree = BinaryTree(5)
    tree.root.left = Node(4)
    tree.root.right = Node(2)
    tree.root.left.left = Node(3)
    tree.root.left.right = Node(3)
    tree.root.right.left = Node(7)
    print(tree.PrintTree())
    dict = tree.GetLevelOrderTraversal()
    print(tree.EvenOddTree(dict))

    tree = BinaryTree(5)
    tree.root.left = Node(9)
    tree.root.right = Node(1)
    tree.root.left.left = Node(3)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(7)
    print(tree.PrintTree())
    dict = tree.GetLevelOrderTraversal()
    print(tree.EvenOddTree(dict))

    tree = BinaryTree(1)
    print(tree.PrintTree())
    dict = tree.GetLevelOrderTraversal()
    print(tree.EvenOddTree(dict))

if __name__=='__main__':
    main()