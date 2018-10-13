'''
Maximum distinct elements after removing k elements
Given an array arr[] containing n elements. The problem is to find maximum number of distinct elements (non-repeating) after removing k elements from the array.
Note: 1 <= k <= n.

Examples:

Input : arr[] = {5, 7, 5, 5, 1, 2, 2}, k = 3
Output : 4
Remove 2 occurrences of element 5 and
1 occurrence of element 2.

Input : arr[] = {1, 2, 3, 4, 5, 6, 7}, k = 5
Output : 2

Input : arr[] = {1, 2, 2, 2}, k = 1
Output : 1
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

        sort_lst=sorted(self.dict.items(),key=lambda x:x[1],reverse=True)
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

    def pop(self):

        freq_num=self.stk[-1]
        node = self.freq[freq_num][-1]
        if freq_num==1:
            if len(self.freq[freq_num])>1:
                self.freq[freq_num].pop()
                del self.dict[node]
            else:
                del self.freq[freq_num]
                del self.dict[node]
                idx=self.stk[freq_num]
                del self.stk[idx]
        else:
            if len(self.freq[freq_num]) > 1:
                self.freq[freq_num].pop()
                freq_num=freq_num-1
                if freq_num in self.freq.keys():
                    self.freq[freq_num].append(node)
                else:
                    tmp=[]
                    tmp.append(node)
                    self.freq[freq_num]=tmp
            else:
                del self.freq[freq_num]
                idx = self.stk.index(freq_num)
                del self.stk[idx]
                freq_num=freq_num-1
                if freq_num in self.freq.keys():
                    self.freq[freq_num].append(node)
                else:
                    tmp=[]
                    tmp.append(node)
                    self.freq[freq_num]=tmp
                if freq_num not in self.stk:
                    self.stk.append(freq_num)
            if node in self.dict.keys():
                self.dict[node]=self.dict.get(node)-1


    def GetDistictElements(self):

        cnt=0
        print(self.dict)
        for key,val in self.dict.items():
            cnt=cnt+1
        return cnt

    def MaxDistinctElementsAfterRemovingKElements(self,ary,k):

        for key in ary:
            self.push(key)
        self.CreateQueue()
        i=0
        while i<k:
            self.pop()
            i=i+1
        return self.GetDistictElements()


def main():

    ary=[5, 7, 5, 5, 1, 2, 2]
    k=3
    stk=PriorityQueue()
    print(stk.MaxDistinctElementsAfterRemovingKElements(ary,k))

    ary = [1, 2, 3, 4, 5, 6, 7]
    k = 5
    stk = PriorityQueue()
    print(stk.MaxDistinctElementsAfterRemovingKElements(ary, k))

    ary = [1, 2, 2, 2]
    k = 1
    stk = PriorityQueue()
    print(stk.MaxDistinctElementsAfterRemovingKElements(ary, k))

if __name__=='__main__':
    main()