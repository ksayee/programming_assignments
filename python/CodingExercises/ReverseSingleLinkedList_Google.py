'''
Reverse a Single Linked List without using extra space
'''

class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def AddNode(self,value):

        start = self.head

        if start is None:
            self.head = Node(value)
        else:
            while start.next is not None:
                start = start.next
            start.next = Node(value)

    def DisplayList(self):

        output_lst = []

        start = self.head
        while start is not None:
            output_lst.append(str(start.value))
            start = start.next
        print(' --> '.join(output_lst))

    def ReverseList(self):

        start = self.head
        self.ReverseList_recur(start)

    def ReverseList_recur(self,start):

        if start.next is None:
            self.head = start
            return start
        tmp_node = start
        return_node = self.ReverseList_recur(start.next)
        return_node.next = tmp_node
        tmp_node.next = None
        return tmp_node

def main():

    LL = LinkedList()
    LL.AddNode(1)
    LL.AddNode(2)
    LL.AddNode(3)
    LL.AddNode(4)
    LL.AddNode(5)
    LL.DisplayList()
    LL.ReverseList()
    LL.DisplayList()

if __name__=='__main__':
    main()