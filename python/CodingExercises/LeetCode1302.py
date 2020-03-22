'''
1302. Deepest Leaves Sum
Given a binary tree, return the sum of values of its deepest leaves.
Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
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

    def DeepestLeavesSum(self):
        start=self.root
        node_lst=[]
        node_lst.append(start)
        node_lst.append('NONE')
        dict={}
        height=1

        while len(node_lst)!=0:
            tmp=[]
            while node_lst[0]!='NONE':
                n=node_lst[0]
                node_lst.pop(0)
                if n.left is None and n.right is None:
                    tmp.append(n.value)
                if n.left!=None:
                    node_lst.append(n.left)
                if n.right!=None:
                    node_lst.append(n.right)
            if node_lst[0]=='NONE' and len(node_lst)==1:
                dict[height]=tmp.copy()
                break
            else:
                dict[height]=tmp.copy()
                node_lst.pop(0)
                node_lst.append('NONE')
            height=height+1
        output_lst=sorted(dict.items(),key=lambda x:x[0],reverse=True)[0][1]

        sum=0
        for item in output_lst:
            sum=sum+item
        return sum

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.left.left.left = Node(7)
    tree.root.right.right = Node(6)
    tree.root.right.right.right = Node(8)
    print(tree.PrintTree())
    print(tree.DeepestLeavesSum())

if __name__=='__main__':
    main()