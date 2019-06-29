'''
Inorder Tree Traversal without Recursion
Using Stack is the obvious way to traverse tree without recursion. Below is an algorithm for traversing binary tree using stack. See this for step wise step execution of the algorithm.
1) Create an empty stack S.
2) Initialize current node as root
3) Push the current node to S and set current = current->left until current is NULL
4) If current is NULL and stack is not empty then
     a) Pop the top item from stack.
     b) Print the popped item, set current = popped_item->right
     c) Go to step 3.
5) If current is NULL and stack is empty then we are done.
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,value):
        self.root=Node(value)

    def InOrder(self,start,tmp):
        if start is None:
            return
        self.InOrder(start.left,tmp)
        tmp.append(str(start.value))
        self.InOrder(start.right,tmp)

    def PrintInorder(self):
        tmp=[]
        start=self.root
        self.InOrder(start,tmp)
        return '-'.join(tmp)

    def InOrderIterative(self):
        curr=self.root
        stk=[]
        fnl_lst=[]

        while curr!=None or len(stk)!=0:
            while curr!=None:
                stk.append(curr)
                curr=curr.left
            tmp=stk[-1]
            stk.pop()
            fnl_lst.append(str(tmp.value))
            curr=tmp.right
        return '-'.join(fnl_lst)

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(4)
    tree.root.left.right=Node(5)
    print(tree.PrintInorder())
    print(tree.InOrderIterative())

if __name__=='__main__':
    main()