'''
895. Maximum Frequency Stack
Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:

push(int x), which pushes an integer x onto the stack.
pop(), which removes and returns the most frequent element in the stack.
If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.


Example 1:

Input:
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

pop() -> returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].

pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].

pop() -> returns 5.
The stack becomes [5,7,4].

pop() -> returns 4.
The stack becomes [5,7].
'''

class stack(object):

    def __init__(self):
        self.stk=[]
        self.freq={}
        self.dict={}

    def push(self,val):

        flg=False
        if val in self.dict.keys():
            self.dict[val]=self.dict.get(val)+1
        else:
            self.dict[val]=1

        freq_num=self.dict[val]

        if freq_num in self.freq.keys():
            self.freq[freq_num].append(val)
            flg=True
        else:
            tmp=[]
            tmp.append(val)
            self.freq[freq_num]=tmp

        if flg==False:
            self.stk.append(freq_num)
        self.display()
        print(self.freq)
        print(self.dict)
        print(self.stk)

    def pop(self):

        itm=self.stk[-1]

        if len(self.freq[itm])==1:
            self.stk.pop()
            value=self.freq[itm][-1]
            del self.freq[itm]
        else:
            value=self.freq[itm][0]
            self.freq[itm].pop()

        if value in self.dict.keys() and self.dict[value]>0:
            self.dict[value]=self.dict.get(value)-1
            if self.dict[value]==0:
                del self.dict[value]
        self.display()
        print(self.freq)
        print(self.dict)
        print(self.stk)

    def display(self):

        for i in range(0,len(self.stk)):
            freq_num=self.stk[i]
            for l in self.freq[freq_num]:
                print(l,end=' ')

def main():

    stk=stack()
    stk.push(5)
    stk.push(7)
    stk.push(5)
    stk.push(7)
    stk.push(4)
    stk.push(5)
    stk.pop()
    stk.pop()
    stk.pop()
    stk.pop()

if __name__=='__main__':
    main()