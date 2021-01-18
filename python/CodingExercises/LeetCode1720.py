'''
1721. Swapping Nodes in a Linked List
You are given the head of a linked list, and an integer k.
Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
Example 3:
Input: head = [1], k = 1
Output: [1]
Example 4:
Input: head = [1,2], k = 1
Output: [2,1]
Example 5:
Input: head = [1,2,3], k = 2
Output: [1,2,3]
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def AddNodes(self,value):
        start = self.head
        node=Node(value)
        if self.head is None:
            self.head = node
        else:
            while start.next is not None:
                start = start.next
            start.next = node

    def SwapValues(self,k):

        cnt = 0
        curr = self.head

        while curr is not None:
            curr = curr.next
            cnt = cnt +1

        left = None
        right = None

        i = 0
        curr = self.head
        while True:
            if i == k-1:
                left = curr

            if i == cnt -k:
                right = curr
                break
            i = i +1
            curr = curr.next

        tmp = left.value
        left.value = right.value
        right.value = tmp

    def DisplayList(self):

        start = self.head
        tmp = []
        while start is not None:
            tmp.append(str(start.value))
            start = start.next
        print('-'.join(tmp))

def main():
    
    ll = LinkedList()
    lst = [1,2,3,4,5]
    k = 2
    for item in lst:
        ll.AddNodes(item)
    ll.DisplayList()
    ll.SwapValues(k)
    ll.DisplayList()

    ll = LinkedList()
    lst = [7,9,6,6,7,8,3,0,9,5]
    k = 5
    for item in lst:
        ll.AddNodes(item)
    ll.DisplayList()
    ll.SwapValues(k)
    ll.DisplayList()

    ll = LinkedList()
    lst = [1]
    k = 1
    for item in lst:
        ll.AddNodes(item)
    ll.DisplayList()
    ll.SwapValues(k)
    ll.DisplayList()

    ll = LinkedList()
    lst = [1, 2]
    k = 1
    for item in lst:
        ll.AddNodes(item)
    ll.DisplayList()
    ll.SwapValues(k)
    ll.DisplayList()

    ll = LinkedList()
    lst = [1,2,3]
    k = 1
    for item in lst:
        ll.AddNodes(item)
    ll.DisplayList()
    ll.SwapValues(k)
    ll.DisplayList()

if __name__=='__main__':
    main()