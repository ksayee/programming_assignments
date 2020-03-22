'''
449. Serialize and Deserialize BST
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.
The encoded string should be as compact as possible.
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
            return None
        tmp.append(str(start.value))
        self.Preorder(start.left,tmp)
        self.Preorder(start.right,tmp)

    def PrintTree(self):
        start=self.root
        tmp=[]
        self.Preorder(start,tmp)
        return '-'.join(tmp)

    def Serialization_recur(self,start,tmp):
        if start is None:
            tmp.append('#')
            return
        tmp.append(str(start.value))
        self.Serialization_recur(start.left,tmp)
        self.Serialization_recur(start.right,tmp)

    def Serialization(self):
        start=self.root
        tmp=[]
        self.Serialization_recur(start,tmp)
        return tmp

    def Deserialization_recur(self,tmp,flg):
        if flg==True:
            d_tree=BinaryTree(tmp[0])
            node=d_tree.root
            tmp.pop(0)
        else:
            if tmp[0]=='#':
                tmp.pop(0)
                return None
            node=Node(tmp[0])
            tmp.pop(0)
        node.left=self.Deserialization_recur(tmp,False)
        node.right=self.Deserialization_recur(tmp,False)
        if flg==False:
            return node
        else:
            return d_tree

    def Deserialization(self,tmp):
        d_tree=self.Deserialization_recur(tmp,True)
        print(d_tree.PrintTree())

def main():

    tree=BinaryTree(12)
    tree.root.left=Node(13)
    print(tree.PrintTree())
    tmp=tree.Serialization()
    print('-'.join(tmp))
    tree.Deserialization(tmp)

    tree = BinaryTree(20)
    tree.root.left = Node(8)
    tree.root.right = Node(22)
    print(tree.PrintTree())
    tmp = tree.Serialization()
    print('-'.join(tmp))
    tree.Deserialization(tmp)

    tree = BinaryTree(20)
    tree.root.left = Node(8)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(12)
    tree.root.left.right.left = Node(10)
    tree.root.left.right.right = Node(14)
    print(tree.PrintTree())
    tmp = tree.Serialization()
    print('-'.join(tmp))
    tree.Deserialization(tmp)

if __name__=='__main__':
    main()