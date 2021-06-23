'''
This problem was asked by Airbnb.
Given a linked list and a positive integer k, rotate the list to the right by k places.
For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.
Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.
'''

class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self,value):
        self.head = Node(value)
        self.length = 1

    def AddNode(self,value):
        node = Node(value)
        start = self.head
        while start.next is not None:
            start = start.next
        start.next = node
        self.length = self.length + 1

    def DisplayList(self):
        output_lst = []
        start = self.head
        while start is not None:
            output_lst.append(str(start.value))
            start = start.next
        print(' --> '.join(output_lst))

    def RotateListByKNodes(self,k=0):

        if k == 0:
            m = 0
        elif k >= self.length:
            m = k % self.length
            m = self.length - m
        else:
            m = self.length - k
        i=1
        curr = self.head
        while i < m:
            curr = curr.next
            i = i +1
        tmp_node = curr

        while curr.next is not None:
            curr = curr.next

        curr.next = self.head
        self.head = tmp_node.next
        tmp_node.next = None
        self.DisplayList()

def main():

    ll = LinkedList(7)
    ll.AddNode(7)
    ll.AddNode(3)
    ll.AddNode(5)
    ll.DisplayList()
    ll.RotateListByKNodes(2)

    ll = LinkedList(1)
    ll.AddNode(2)
    ll.AddNode(3)
    ll.AddNode(4)
    ll.AddNode(5)
    ll.DisplayList()
    ll.RotateListByKNodes(3)

if __name__=='__main__':
    main()