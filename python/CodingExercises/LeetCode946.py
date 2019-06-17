'''
946. Validate Stack Sequences
Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.
Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
Note:

0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed is a permutation of popped.
pushed and popped have distinct values.
'''

class Stack(object):
    def __init__(self):
        self.stk=[]

    def Add(self,value):
        self.stk.append(value)

    def Peek(self):
        if len(self.stk)==0:
            return -999
        else:
            return self.stk[-1]

    def Pop(self):
        self.stk.pop()

    def Display(self):
        print(self.stk)

def LeetCode946(pushed,popped):

    stk=Stack()
    k=0
    for i in range(0,len(pushed)):
        if stk.Peek()==-999:
            stk.Add(pushed[i])
        elif stk.Peek()!=popped[k]:
            stk.Add(pushed[i])
        else:
            while stk.Peek()!=-999 and stk.Peek()==popped[k]:
                k=k+1
                stk.Pop()
            stk.Add(pushed[i])

    for j in range(k,len(popped)):
        if stk.Peek()!=popped[j]:
            return False
        else:
            stk.Pop()

    if stk.Peek()==-999:
        return True
    else:
        return False

def main():

    pushed=[1,2,3,4,5]
    popped=[4,5,3,2,1]
    print(LeetCode946(pushed,popped))

    pushed = [1,2,3,4,5]
    popped = [4,3,5,1,2]
    print(LeetCode946(pushed, popped))


if __name__=='__main__':
    main()