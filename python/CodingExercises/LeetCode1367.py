'''
1367. Linked List in Binary Tree
Given a binary tree root and a linked list with head as the first node.
Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.
In this context downward path means a path that starts at some node and goes downwards.
Example 1:
Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.
Example 2:
Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Example 3:
Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.
'''

class TreeNode(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class LinkedListNode(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class BinaryTree(object):
    def __init__(self,value):
        self.root = TreeNode(value)

    def PrintTree(self):
        tmp = []
        start = self.root
        self.Preorder(start,tmp)
        print(' - '.join(tmp))

    def Preorder(self,start,tmp):
        if start is None:
            return
        tmp.append(str(start.value))
        self.Preorder(start.left,tmp)
        self.Preorder(start.right,tmp)

    def CheckLinkedListinTree(self,ll_obj):
        ll_head = ll_obj.head
        tree_start = self.root
        flg = self.CheckLinkedListinTree_recur(ll_head,tree_start)
        return flg

    def CheckLinkedListinTree_recur(self,ll_head,tree_start):
        if ll_head is None:
            return True
        if tree_start is None:
            return False
        if ll_head.value == tree_start.value:
            return self.CheckLinkedListinTree_recur(ll_head.next,tree_start.left) or self.CheckLinkedListinTree_recur(ll_head.next,tree_start.right)
        else:
            return self.CheckLinkedListinTree_recur(ll_head,tree_start.left) or self.CheckLinkedListinTree_recur(ll_head,tree_start.right)

class LinkedList(object):
    def __init__(self,value):
        self.head = LinkedListNode(value)

    def AddNode(self,value):
        node = LinkedListNode(value)
        start = self.head
        while start.next is not None:
            start = start.next
        start.next = node

    def DisplayList(self):

        output_list = []
        start = self.head
        while start is not None:
            output_list.append(str(start.value))
            start = start.next
        print(' --> '.join(output_list))

def main():

    ll = LinkedList(4)
    ll.AddNode(2)
    ll.AddNode(8)
    ll.DisplayList()

    tree = BinaryTree(1)
    tree.root.left = TreeNode(4)
    tree.root.right = TreeNode(4)
    tree.root.left.right = TreeNode(2)
    tree.root.left.right.left = TreeNode(1)
    tree.root.right.left = TreeNode(2)
    tree.root.right.left.left = TreeNode(6)
    tree.root.right.left.right = TreeNode(8)
    tree.root.right.left.right.left = TreeNode(1)
    tree.root.right.left.right.right = TreeNode(3)
    tree.PrintTree()
    print(tree.CheckLinkedListinTree(ll))

if __name__=='__main__':
    main()