'''
1172. Dinner Plate Stacks
You have an infinite number of stacks arranged in a row and numbered (left to right) from 0, each of the stacks has the same maximum capacity.
Implement the DinnerPlates class:
DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks.
void push(int val) pushes the given positive integer val into the leftmost stack with size less than capacity.
int pop() returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns -1 if all stacks are empty.
int popAtStack(int index) returns the value at the top of the stack with the given index and removes it from that stack, and returns -1 if the stack with that given index is empty.
Example:
Input:
["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
Output:
[null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]
Explanation:
DinnerPlates D = DinnerPlates(2);  // Initialize with capacity = 2
D.push(1);
D.push(2);
D.push(3);
D.push(4);
D.push(5);         // The stacks are now:  2  4
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.popAtStack(0);   // Returns 2.  The stacks are now:     4
                                                       1  3  5
                                                       ﹈ ﹈ ﹈
D.push(20);        // The stacks are now: 20  4
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.push(21);        // The stacks are now: 20  4 21
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.popAtStack(0);   // Returns 20.  The stacks are now:     4 21
                                                        1  3  5
                                                        ﹈ ﹈ ﹈
D.popAtStack(2);   // Returns 21.  The stacks are now:     4
                                                        1  3  5
                                                        ﹈ ﹈ ﹈
D.pop()            // Returns 5.  The stacks are now:      4
                                                        1  3
                                                        ﹈ ﹈
D.pop()            // Returns 4.  The stacks are now:   1  3
                                                        ﹈ ﹈
D.pop()            // Returns 3.  The stacks are now:   1
                                                        ﹈
D.pop()            // Returns 1.  There are no stacks.
D.pop()            // Returns -1.  There are still no stacks.
'''

class DinnerPlates(object):
    def __init__(self,size):
        self.stk=[]
        self.dict={}
        self.stk_size=size

    def Push(self,value):
        if len(self.stk)==0:
            self.stk.append(0)
            self.dict[0]=[]
            self.dict[0].append(value)
        else:
            flg=False
            for i in range(0,len(self.stk)):
                key=self.stk[i]
                if len(self.dict[key])<self.stk_size:
                    self.dict[key].append(value)
                    flg=True
                    break
                elif len(self.dict[key])==self.stk_size:
                    pass
            if flg==False:
                num=self.stk[-1]+1
                self.stk.append(num)
                self.dict[num]=[]
                self.dict[num].append(value)
        self.Display()

    def PopAtStack(self,stk_num):
        if stk_num in self.dict.keys():
            self.dict[stk_num].pop()
            if len(self.dict[stk_num])==0:
                del self.dict[stk_num]
                idx=self.stk.index(stk_num)
                del self.stk[idx]
        else:
            print("INVALID STACK NUM")
        self.Display()

    def Pop(self):
        if len(self.stk)==0:
            print("STACK IS EMPTY")
        else:
            num=self.stk[-1]
            self.dict[num].pop()
            if len(self.dict[num])==0:
                del self.dict[num]
                idx=self.stk.index(num)
                del self.stk[idx]
        self.Display()

    def Display(self):
        print("Starting Display Stack")
        for i in range(0,len(self.stk)):
            key=self.stk[i]
            print(self.dict[key])
        print("End Display of Stack")

def main():

    actions=["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
    values=[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
    i=0
    for action in actions:
        if action=="DinnerPlates":
            dp=DinnerPlates(values[i][0])
        elif action=="push":
            dp.Push(values[i][0])
        elif action=="popAtStack":
            dp.PopAtStack(values[i][0])
        elif action=="pop":
            dp.Pop()
        i=i+1

if __name__=='__main__':
    main()