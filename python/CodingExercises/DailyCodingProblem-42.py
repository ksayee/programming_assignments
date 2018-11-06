'''
This problem was asked by Google.
Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.
Integers can appear more than once in the list. You may assume all numbers in the list are positive.
For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
'''

import collections
def DailyCodingProblem42(ary,k):

    dict=collections.Counter(ary)

    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,k)

    return fnl_lst

def Combinations_recur(lst,cnt,tmp,fnl_lst,k):

    if k==0:
        if sorted(tmp) not in fnl_lst:
            fnl_lst.append(sorted(tmp).copy())
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue

        if k<0:
            break
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst, k-lst[i])
        cnt[i]=cnt[i]+1
        tmp.pop()

def main():

    ary=[12, 1, 61, 5, 9, 2]
    k=24
    print(DailyCodingProblem42(ary,k))

if __name__=='__main__':
    main()