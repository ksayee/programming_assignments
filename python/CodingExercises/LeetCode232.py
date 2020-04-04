'''
232. Implement Queue using Stacks
Implement the following operations of a queue using stacks.
push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:
MyQueue queue = new MyQueue();
queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
'''

class Queue(object):
    def __init__(self):
        self.stk=[]

    def Push(self,value):
        self.stk.append(value)

    def Peek(self):
        return self.stk[0]
    def Pop(self):
        if len(self.stk)==0:
            return "Stack is Empty"
        else:
            num=self.stk[0]
            self.stk.pop(0)
            return num

    def Empty(self):
        if len(self.stk)==0:
            return True
        else:
            return False


def main():

    q=Queue()
    q.Push(1)
    q.Push(2)
    print(q.Peek())
    print(q.Pop())
    print(q.Empty())

if __name__=='__main__':
    main()