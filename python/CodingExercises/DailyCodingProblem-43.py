'''
This problem was asked by Amazon.
Implement a stack that has the following methods:
push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
'''

class Stack(object):

    def __init__(self):
        self.stk=[]
        self.max_stk=[]

    def push(self,value):

        if len(self.stk)==0:
            self.stk.append(value)
            self.max_stk.append(value)
        else:
            self.stk.append(value)
            if value>self.max_stk[-1]:
                self.max_stk.append(value)
        print(self.print_stack())

    def pop(self):

        if len(self.stk)>0:
            self.stk.pop()
        print(self.print_stack())
        print("Maximum Element:",self.return_max())

    def print_stack(self):

        fnl_lst=[]

        for l in self.stk:
            fnl_lst.append(str(l))
        return '-'.join(fnl_lst)

    def return_max(self):

        if len(self.max_stk)>0:
            n=self.max_stk[-1]
            self.max_stk.pop()
        else:
            n=-1
        return n

def main():

    stk=Stack()
    stk.push(10)
    stk.push(9)
    stk.push(8)
    stk.push(11)
    stk.push(15)
    stk.push(12)
    stk.push(13)
    stk.pop()
    stk.pop()
    stk.pop()
    stk.pop()
    stk.pop()
    stk.pop()

if __name__=='__main__':
    main()