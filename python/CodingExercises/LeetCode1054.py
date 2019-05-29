'''
1054. Distant Barcodes
Share
In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].
Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any answer, and it is guaranteed an answer exists.
Example 1:

Input: [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
Example 2:

Input: [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,2,1,2,1]

Note:

1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000

'''

import collections
class PriorityQueue(object):

    def __init__(self):
        self.stk=[]
        self.dict={}
        self.freq={}

    def CreateQueue(self,ary):

        self.dict=collections.Counter(ary)
        sort_dict=sorted(self.dict.items(),key=lambda x:x[1])

        for i in range(0,len(sort_dict)):
            itm=sort_dict[i][0]
            frq=sort_dict[i][1]

            if frq in self.freq.keys():
                self.freq[frq].append(itm)
            else:
                tmp=[]
                tmp.append(itm)
                self.freq[frq]=tmp
                self.stk.append(frq)

    def pop(self):

        lst=[]
        frq=self.stk[-1]
        if len(self.freq[frq])>1:
            lst.append(self.freq[frq][0])
            lst.append(self.freq[frq][1])
        else:
            lst.append(self.freq[frq][0])
            if len(self.stk)>1:
                frq2=self.stk[-2]
                lst.append(self.freq[frq2][0])
        return lst

    def rearrange(self,lst):

        for i in range(0,len(lst)):
            key=lst[i]
            frq=self.dict[key]
            if frq>1:
                self.dict[key]=frq-1
            else:
                del self.dict[key]

            if frq>1:
                for j in range(0,len(self.freq[frq])):
                    if key==self.freq[frq][j]:
                        del self.freq[frq][j]
                        break
                if len(self.freq[frq])==0:
                    del self.freq[frq]
                    idx=self.stk.index(frq)
                    del self.stk[idx]
                if frq-1 in self.freq.keys():
                    self.freq[frq-1].append(key)
                else:
                    tmp=[]
                    tmp.append(key)
                    self.freq[frq-1]=tmp
                    self.stk.append(frq-1)
            else:
                for j in range(0, len(self.freq[frq])):
                    if key == self.freq[frq][j]:
                        del self.freq[frq][j]
                        break
                if len(self.freq[frq]) == 0:
                    del self.freq[frq]
                    idx = self.stk.index(frq)
                    del self.stk[idx]

    def CreateList(self,ary):

        self.CreateQueue(ary)
        fnl_lst=[]
        while True:
            lst=self.pop()
            if len(fnl_lst)==0:
                fnl_lst.append(lst[0])
                fnl_lst.append(lst[1])
                self.rearrange(lst)
            elif len(lst)>1:
                if fnl_lst[-1]!=lst[0]:
                    fnl_lst.append(lst[0])
                    del lst[1]
                elif fnl_lst[-1]!=lst[1]:
                    fnl_lst.append(lst[1])
                    del lst[0]
                self.rearrange(lst)
            else:
                if fnl_lst[-1]!=lst[0]:
                    fnl_lst.append(lst[0])
                    del lst[0]
            if len(lst)==0:
                break
        return fnl_lst

def main():

    ary=[1,1,1,1,2,2,3,3]
    stk=PriorityQueue()
    print(stk.CreateList(ary))

    ary = [1,1,1,2,2,2]
    stk = PriorityQueue()
    print(stk.CreateList(ary))

    ary=list('aaabc')
    stk = PriorityQueue()
    print(stk.CreateList(ary))

    ary = list('aaabb')
    stk = PriorityQueue()
    print(stk.CreateList(ary))

if __name__=='__main__':
    main()