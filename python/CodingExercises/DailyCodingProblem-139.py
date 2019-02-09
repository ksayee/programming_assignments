'''
This problem was asked by Google.
Given an iterator with methods next() and hasNext(), create a wrapper iterator, PeekableInterface, which also implements peek(). peek shows the next element that would be returned on next().
Here is the interface:
class PeekableInterface(object):
    def __init__(self, iterator):
        pass

    def peek(self):
        pass

    def next(self):
        pass

    def hasNext(self):
        pass
'''

class PeekableInterface(object):
    def __init__(self,value):
        self.stk=[]
        self.stk.append(value)

    def add(self,value):
        self.stk.append(value)

    def display(self):
        for l in self.stk:
            print(l,end=' ')

    def next(self):
        ele=self.stk[0]
        self.stk.pop(0)
        return ele

    def hasNext(self):

        if len(self.stk)==0:
            return False
        else:
            return True

    def peek(self):
        return self.stk[0]

def main():

    ary=[2, 4, 6, 8, 10, 2, 6, 10]
    ll=PeekableInterface(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)
    ll.display()
    print(ll.next())
    print(ll.hasNext())
    print(ll.peek())
    print(ll.next())

if __name__=='__main__':
    main()