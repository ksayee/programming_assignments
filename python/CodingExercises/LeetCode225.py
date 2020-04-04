'''
225. Implement Stack using Queues
Implement the following operations of a stack using queues.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:
MyStack stack = new MyStack();
stack.push(1);
stack.push(2);
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
'''

class Stack(object):
    def __init__(self):
        self.queue=[]

    def Push(self,value):
        self.queue.append(value)

    def Top(self):
        return self.queue[-1]

    def Pop(self):
        if len(self.queue)==0:
            return "Queue is Empty"
        else:
            num=self.queue[-1]
            self.queue.pop()
            return num

    def Empty(self):
        if len(self.queue)==0:
            return True
        else:
            return False


def main():

    stk=Stack()
    stk.Push(1)
    stk.Push(2)
    print(stk.Top())
    print(stk.Pop())
    print(stk.Empty())

if __name__=='__main__':
    main()