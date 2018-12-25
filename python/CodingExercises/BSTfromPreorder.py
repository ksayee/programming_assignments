'''
Given preorder traversal of a binary search tree, construct the BST.
For example, if the given traversal is {10, 5, 1, 7, 40, 50}, then the output should be root of following tree.
     10
   /   \
  5     40
 /  \      \
1    7      50
We have discussed O(n^2) and O(n) recursive solutions in the previous post. Following is a stack based iterative solution that works in O(n) time.
1. Create an empty stack.
2. Make the first value as root. Push it to the stack.
3. Keep on popping while the stack is not empty and the next value is greater than stack’s top value. Make this value as the right child of the last popped node. Push the new node to the stack.
4. If the next value is less than the stack’s top value, make this value as the left child of the stack’s top node. Push the new node to the stack.
5. Repeat steps 2 and 3 until there are items remaining in pre[].
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,root):
        self.root=Node(root)

    def preorder(self,start,tmp):
        if start is None:
            return
        tmp.append(start.value)
        self.preorder(start.left,tmp)
        self.preorder(start.right,tmp)

    def BSTfromPreorder(self,ary):
        stk=[]
        start=self.root
        stk.append(start)
        for i in range(1,len(ary)):
            tmp=None
            key=ary[i]
            while len(stk)!=0 and key>stk[-1].value:
                tmp=stk[-1]
                stk.pop()
            if tmp==None:
                stk[-1].left=Node(key)
                stk.append(stk[-1].left)
            else:
                tmp.right=Node(key)
                stk.append(tmp.right)
        fnl_lst=[]
        self.preorder(start,fnl_lst)
        return fnl_lst

    def PrintTraversal(self,traversaltype):
        tmp=[]
        start=self.root
        if traversaltype=='Preorder':
            self.preorder(start,tmp)
        return tmp

def main():

    ary=[10, 5, 1, 7, 40, 50]
    tree=BinaryTree(ary[0])
    print(tree.BSTfromPreorder(ary))

if __name__=='__main__':
    main()