'''
716. Max Stack
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5);
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
'''

class stack(object):

    def __init__(self):
        self.stk=[]
        self.max_stk=[]

    def push(self,val):

        if len(self.stk)==0:
            self.stk.append(val)
            self.max_stk.append(val)
        else:
            if val>self.max_stk[-1]:
                self.max_stk.append(val)
            else:
                self.max_stk.append(self.max_stk[-1])
            self.stk.append(val)
        self.display()

    def pop(self):

        self.stk.pop()
        self.max_stk.pop()
        self.display()

    def peekMax(self):

        return self.max_stk[-1]

    def display(self):

        for i in range(0,len(self.stk)):
            print(self.stk[i],end=' ')
        print("Max Value:",self.max_stk[-1])

def main():

    stk=stack()
    stk.push(10)
    stk.push(20)
    stk.push(5)
    stk.push(15)
    stk.push(30)
    stk.pop()
    stk.pop()
    stk.push(40)
    print(stk.peekMax())

if __name__=='__main__':
    main()