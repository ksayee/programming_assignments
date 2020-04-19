'''
This problem was asked by Google.
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
In this example, assume nodes with the same value are the exact same node objects.
Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
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

    def GetLength(self,start):
        cnt=1
        while start.next!=None:
            start=start.next
            cnt=cnt+1
        return cnt

    def GetIntersection(self,L2):
        start1=self.head
        start2=L2.head
        Len1=self.GetLength(start1)
        Len2=self.GetLength(start2)

        diff=abs(Len1-Len2)

        if Len1>Len2:
            while diff >0:
                start1=start1.next
                diff=diff-1
        elif Len2>Len1:
            while diff >0:
                start2=start2.next
                diff=diff-1
        else:
            pass

        while start1!=None and start2!=None:
            if start1.value==start2.value:
                return start1.value
            else:
                start1=start1.next
                start2=start2.next
        return None

def main():

    L1=LinkedList()
    L1.Add(3)
    L1.Add(7)
    L1.Add(8)
    L1.Add(10)

    L2 = LinkedList()
    L2.Add(99)
    L2.Add(1)
    L2.Add(8)
    L2.Add(10)
    print(L1.GetIntersection(L2))
    
if __name__=='__main__':
    main()