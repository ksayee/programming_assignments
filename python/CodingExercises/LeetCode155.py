'''
155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

class stack(object):

    def __init__(self):
        self.stk=[]
        self.min_stk=[]

    def push(self,val):

        if len(self.stk)==0:
            self.stk.append(val)
            self.min_stk.append(val)
        else:
            if val<self.min_stk[-1]:
                self.min_stk.append(val)
            else:
                self.min_stk.append(self.min_stk[-1])
            self.stk.append(val)
        self.display()

    def pop(self):

        self.stk.pop()
        self.min_stk.pop()
        self.display()

    def peekMin(self):

        return self.min_stk[-1]

    def display(self):

        for i in range(0,len(self.stk)):
            print(self.stk[i],end=' ')
        print("Min Value:",self.min_stk[-1])

def main():

    stk=stack()
    stk.push(-2)
    stk.push(0)
    stk.push(-3)
    stk.pop()
    stk.pop()

if __name__=='__main__':
    main()