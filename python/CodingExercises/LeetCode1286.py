'''
1286. Iterator for Combination
Medium
Design an Iterator class, which has:
A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.
Example:
CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.
iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false
'''

import collections
class CombinationIterator(object):
    def __init__(self,str1,length):
        self.lst=[]
        self.cnt=[]
        self.tmp_lst=[]
        self.output_lst=[]
        self.dict=collections.Counter(str1)
        self.lenght=length
        for key,val in self.dict.items():
            self.lst.append(key)
            self.cnt.append(val)
        self.GetCombinations()

    def Combinations_recur(self):

        if len(self.tmp_lst)==self.lenght:
            self.output_lst.append(''.join(self.tmp_lst))
            return

        for i in range(0,len(self.lst)):
            if self.cnt[i]==0:
                continue
            self.tmp_lst.append(self.lst[i])
            self.cnt[i]=self.cnt[i]-1
            self.Combinations_recur()
            self.cnt[i]=self.cnt[i]+1
            self.tmp_lst.pop()

    def GetCombinations(self):
        self.Combinations_recur()
        self.output_lst.sort()

    def GetNext(self):

        if len(self.output_lst)>0:
            item=self.output_lst[0]
            self.output_lst.pop(0)
            return item
        else:
            return "No Item"
        
def main():

    cmb=CombinationIterator("abc",2)
    print(cmb.GetNext())
    print(cmb.GetNext())
    print(cmb.GetNext())
    print(cmb.GetNext())
    print(cmb.GetNext())
    print(cmb.GetNext())
    print(cmb.GetNext())
    print(cmb.GetNext())
    print(cmb.GetNext())

if __name__=='__main__':
    main()