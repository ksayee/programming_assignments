# Construct a Complete Binary Tree from a List.
# The list is a level order traversal.

class Node(object):
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,value):
        self.root=Node(value)

    def PrintInOrder(self,start,tmp):

        if start is None:
            return
        self.PrintInOrder(start.left, tmp)
        tmp.append(str(start.data))
        self.PrintInOrder(start.right,tmp)

    def InOrderTraversal(self):

        start=self.root
        tmp=[]
        self.PrintInOrder(start,tmp)
        return tmp

def ConstructCompleteBinaryTreeFromList(lst):

    queue=[]

    for i in range(0,len(lst)):
        if i==0:
            tree=BinaryTree(lst[i])
            queue.append(tree.root)
        else:
            node=queue[0]
            if node.left is None:
                node.left=Node(lst[i])
                queue.append(node.left)
            elif node.right is None:
                node.right=Node(lst[i])
                queue.append(node.right)
                queue.pop(0)

    tmp=tree.InOrderTraversal()
    return '-'.join(tmp)

def main():

    lst=[10,12,15,25,30,36]
    print(ConstructCompleteBinaryTreeFromList(lst))

    lst = [1, 2, 3, 4, 5, 6]
    print(ConstructCompleteBinaryTreeFromList(lst))

    lst = [1, 2, 3, 4, 5, 6, 6, 6, 6, 6]
    print(ConstructCompleteBinaryTreeFromList(lst))

if __name__=='__main__':
    main()