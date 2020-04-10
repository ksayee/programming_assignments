'''
430. Flatten a Multilevel Doubly Linked List
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.
Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.
Example 1:
Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:
The multilevel linked list in the input is as follows:
After flattening the multilevel linked list it becomes:
Example 2:
Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL
Example 3:
Input: head = []
Output: []
How multilevel linked list is represented in test case:
We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The serialization of each level is as follows:
1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
To serialize all levels together we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:
[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
Merging the serialization of each level and removing trailing nulls we obtain:
[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
        self.child=None

class LinkedList(object):
    def __init__(self):
        self.head=None

    def CreateLinkedList(self,lst):
        start=self.head
        flg=False
        for element in lst:
            if element!=None:
                node = Node(element)
                if start is None:
                    start=node
                    self.head=start
                    pntr=start
                else:
                    if flg==True:
                        start.child=node
                        flg=False
                        start=start.child
                        pntr=start
                    else:
                        start.next=node
                        node.prev=start
                        start=start.next
            else:
                if flg==False:
                    flg=True
                    start=pntr
                else:
                    start=start.next


    def FlattenLinkedList(self):
        stk=[]
        start=self.head
        while start!=None:
            prev = start
            if start.child is None:
                start=start.next
            else:
                if start.next is None:
                    start.next=start.child
                    start.child=None
                    start=start.next
                else:
                    stk.append(start.next)
                    start.next=start.child
                    start.child=None
                    start=start.next
        start=prev
        while len(stk)!=0:
            node=stk[-1]
            stk.pop()
            start.next=node
            node.prev=start
            while start.next!=None:
                start=start.next

    def DisplayList(self):
        start=self.head
        tmp=[]
        while start!=None:
            tmp.append(start.value)
            start=start.next
        return tmp

def main():

    link1=LinkedList()
    lst = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10, None, None, 11, 12]
    link1.CreateLinkedList(lst)
    link1.FlattenLinkedList()
    print(link1.DisplayList())

    link2 = LinkedList() 
    lst = [1,2,None,3]
    link2.CreateLinkedList(lst)
    link2.FlattenLinkedList()
    print(link2.DisplayList())


if __name__=='__main__':
    main()