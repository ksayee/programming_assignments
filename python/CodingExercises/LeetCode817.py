'''
817. Linked List Components
We are given head, the head node of a linked list containing unique integer values.
We are also given the list G, a subset of the values in the linked list.
Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.
Example 1:
Input:
head: 0->1->2->3
G = [0, 1, 3]
Output: 2
Explanation:
0 and 1 are connected, so [0, 1] and [3] are the two connected components.
Example 2:
Input:
head: 0->1->2->3->4
G = [0, 3, 1, 4]
Output: 2
Explanation:
0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=None

    def Add(self,value):
        n=Node(value)
        if self.head is None:
            self.head=n
        else:
            start=self.head
            while start.next!=None:
                start=start.next
            start.next=n

    def GetConnectedComponents(self,ary):
        start=self.head
        output_lst=[]
        tmp=[]
        flg=False
        while start!=None:
            tmp=[]
            while start.value in ary:
                flg=True
                tmp.append(start.value)
                start=start.next
                if start is None:
                    break
            output_lst.append(tmp.copy())
            flg=False
            if start is None:
                break
            else:
                start=start.next
        return output_lst

def main():

    LL=LinkedList()
    LL.Add(0)
    LL.Add(1)
    LL.Add(2)
    LL.Add(3)
    ary=[0,1,3]
    print(LL.GetConnectedComponents(ary))

    LL = LinkedList()
    LL.Add(0)
    LL.Add(1)
    LL.Add(2)
    LL.Add(3)
    LL.Add(4)
    ary = [0, 3,1,4]
    print(LL.GetConnectedComponents(ary))

if __name__=='__main__':
    main()