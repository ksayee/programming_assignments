# Given a Singly linkedin list. Reverse it.

class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=None

    def add(self,value):
        node=Node(value)
        if self.head==None:
            self.head=node
        else:
            start=self.head
            while start.next!=None:
                start=start.next
            start.next=node

    def display(self):
        lst=[]
        start=self.head
        while start!=None:
            lst.append(str(start.value))
            start=start.next
        return '-'.join(lst)

    def reverse(self):
        prev_node=None
        curr_node=self.head
        next_node=None

        while curr_node!=None:
            next_node=curr_node.next
            curr_node.next=prev_node
            prev_node=curr_node
            curr_node=next_node
        self.head=prev_node

def main():
    ll=LinkedList()
    ll.add(10)
    ll.add(20)
    ll.add(30)
    ll.add(40)
    print(ll.display())
    ll.reverse()
    print(ll.display())

if __name__=='__main__':
    main()