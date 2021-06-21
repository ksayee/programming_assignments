'''
Given a singly Linked list, rotate it by K nodes.

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

        start = self.head
        output_lst = []
        while start is not None:
            output_lst.append(str(start.value))
            start = start.next
        print(' --> '.join(output_lst))

    def RotateByKNodes(self,k=0):

        if k==0:
            self.DisplayList()
        else:
            if k > self.length:
                k = k % self.length

            m = self.length - k
            curr = self.head
            i = 1
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

    ll = LinkedList(1)
    ll.AddNode(2)
    ll.AddNode(3)
    ll.AddNode(4)
    ll.AddNode(5)
    ll.DisplayList()
    ll.RotateByKNodes(k=12)

if __name__=='__main__':
    main()