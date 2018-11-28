# Build a queue class with Enqueue and Dequeue methods
# The queue should store an unbounded number of elements, but each built-in collection or list you use shoud hold at most 5 elements

class QueueUnboundedNumElements(object):

    def __init__(self):
        self.stk=[]
        self.dict={}

    def enqueue(self,value):
        if len(self.stk)==0:
            n=0
            self.dict[n]=[]
            self.dict[n].append(value)
            self.stk.append(n)
        else:
            n=self.stk[-1]
            lst=self.dict[n]
            if len(lst)<5:
                self.dict[n].append(value)
            else:
                n=n+1
                self.dict[n]=[]
                self.dict[n].append(value)
                self.stk.append(n)

    def dequeue(self):
        if len(self.stk)==0:
            print('Nothing to Dequeue')
        else:
            n=self.stk[0]
            element=self.dict[n][0]
            self.dict[n].pop(0)
            if len(self.dict[n])==0:
                del self.dict[n]
                self.stk.pop(0)
            return element

    def printQueue(self):
        if len(self.stk)==0:
            print('Queue is Empty')
        else:
            print(' ')
            n=self.stk[0]
            while n in self.dict.keys():
                lst=self.dict[n]
                print(lst,end=' ')
                n=n+1

def main():

    q=QueueUnboundedNumElements()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)
    q.enqueue(9)
    q.enqueue(10)
    q.enqueue(11)
    q.enqueue(12)
    q.enqueue(13)
    q.enqueue(14)
    q.enqueue(15)
    q.printQueue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.printQueue()
    q.dequeue()
    q.printQueue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.printQueue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.printQueue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.printQueue()

if __name__=='__main__':
    main()