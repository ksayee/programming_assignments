'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list. Return the linked list sorted as well.
Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]
'''

class Node(object):
    def __init__(self,val):
        self.value=val
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=None

    def AddNode(self,val):
        start=self.head

        node=Node(val)
        if self.head is None:
            self.head=node
        else:
            while start.next is not None:
                start=start.next
            start.next=node

    def RemoveDuplicates(self):

        curr=self.head
        while curr.next is not None:
            if curr.value == curr.next.value:
                if curr == self.head:
                    self.head=curr.next
                else:
                    curr.next = curr.next.next
            curr=curr.next

    def DisplayList(self):

        start = self.head
        tmp = []
        while start is not None:
            tmp.append(str(start.value))
            start=start.next
        print('-'.join(tmp))

def main():

    ll=LinkedList()
    lst=[1,2,3,3,4,4,5]
    for num in lst:
        ll.AddNode(num)
    ll.DisplayList()
    ll.RemoveDuplicates()
    ll.DisplayList()

    ll = LinkedList()
    lst = [1,1,1,2,3]
    for num in lst:
        ll.AddNode(num)
    ll.DisplayList()
    ll.RemoveDuplicates()
    ll.DisplayList()


if __name__=='__main__':
    main()