'''
Find k numbers with most occurrences in the given array
Given an array of n numbers and a positive integer k. The problem is to find k numbers with most occurrences, i.e., the top k numbers having the maximum frequency. If two numbers have same frequency then the larger number should be given preference. The numbers should be displayed in decreasing order of their frequencies. It is assumed that the array consists of k numbers with most occurrences.

Examples:

Input : arr[] = {3, 1, 4, 4, 5, 2, 6, 1},
             k = 2
Output : 4 1
Frequency of 4 = 2
Frequency of 1 = 2
These two have the maximum frequency and
4 is larger than 1.

Input : arr[] = {7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9},
            k = 4
Output : 5 11 7 10
'''

class PriorityQueue(object):

    def __init__(self):
        self.stk=[]
        self.dict={}
        self.freq={}

    def push(self,val):
        if val in self.dict.keys():
            self.dict[val]=self.dict.get(val)+1
        else:
            self.dict[val]=1

    def CreateQueue(self):

        sort_lst=sorted(self.dict.items(),key=lambda x:x[1])
        for key in sort_lst:
            freq_num=key[1]
            if freq_num in self.freq.keys():
                self.freq[freq_num].append(key[0])
            else:
                tmp=[]
                tmp.append(key[0])
                self.freq[freq_num]=tmp

            if freq_num not in self.stk:
                self.stk.append(freq_num)
        for key, val in self.freq.items():
            self.freq[key]=sorted(self.freq[key])

    def pop(self):

        freq_num=self.stk[-1]
        node = self.freq[freq_num][-1]
        if len(self.freq[freq_num])>1:
            self.freq[freq_num].pop()
        else:
            del self.freq[freq_num]
            idx=self.stk.index(freq_num)
            del self.stk[idx]

        return node

    def FindKNumbersWithMostOccurencesGivenArray(self,ary,k):

        for key in ary:
            self.push(key)
        self.CreateQueue()
        i=0
        fnl_lst=[]
        while i<k:
            fnl_lst.append(self.pop())
            i=i+1
        return fnl_lst

def main():

    ary=[3, 1, 4, 4, 5, 2, 6, 1]
    k=2
    stk=PriorityQueue()
    print(stk.FindKNumbersWithMostOccurencesGivenArray(ary,k))

    ary = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9]
    k = 4
    stk = PriorityQueue()
    print(stk.FindKNumbersWithMostOccurencesGivenArray(ary, k))

if __name__=='__main__':
    main()