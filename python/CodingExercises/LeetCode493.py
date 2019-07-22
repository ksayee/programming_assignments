'''
493. Reverse Pairs
Hard
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].
You need to return the number of important reverse pairs in the given array.
Example1:
Input: [1,3,2,3,1]
Output: 2
Example2:
Input: [2,4,3,5,1]
Output: 3
'''

import collections

def Combinations_recur(lst,cnt,tmp,fnl_lst):

    if len(tmp)==2:
        if ''.join(sorted(tmp)) in fnl_lst.keys():
            fnl_lst[''.join(sorted(tmp))].append(tmp.copy())
        else:
            fnl_lst[''.join(sorted(tmp))]=[]
            fnl_lst[''.join(sorted(tmp))].append(tmp.copy())


    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(str(lst[i]))
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst)
        tmp.pop()
        cnt[i]=cnt[i]+1

def LeetCode493(ary):

    dict=collections.Counter(ary)
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    fnl_lst={}
    Combinations_recur(lst,cnt,tmp,fnl_lst)

    cnt=0
    for key,val in fnl_lst.items():
        sample_ary=ary.copy()
        for tup in val:
            idx_lst=[]
            flg=True
            for l in tup:
                try:
                    idx=sample_ary.index(int(l))
                    idx_lst.append(idx)
                    sample_ary[idx]=-9999
                except:
                    flg=False
            if flg==True:
                if sorted(idx_lst)==idx_lst and ary[idx_lst[0]]>2*ary[idx_lst[1]]:
                    cnt=cnt+1
    return cnt

def main():

    ary=[1,3,2,3,1]
    print(LeetCode493(ary))

    ary = [2,4,3,5,1]
    print(LeetCode493(ary))

if __name__=='__main__':
    main()