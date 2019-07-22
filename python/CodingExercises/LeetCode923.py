'''
923. 3Sum With Multiplicity
Medium
Given an integer array A, and an integer target, return the number of tuples i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target.
As the answer can be very large, return it modulo 10^9 + 7.
Example 1:
Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation:
Enumerating by the values (A[i], A[j], A[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
Example 2:
Input: A = [1,1,2,2,2,2], target = 5
Output: 12
Explanation:
A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.
'''

import collections

def ValidateArray(tmp,ary):

    idx_lst=[]
    for element in tmp:
        idx=ary.index(element)
        idx_lst.append(idx)

    if sorted(idx_lst)==idx_lst:
        return True
    else:
        return False

def CheckTarget(tmp,target):

    for element in tmp:
        target=target-element
    if target==0:
        return True
    else:
        return False

def Combinations_recur(lst,cnt,tmp,fnl_lst,target,ary):

    if len(tmp)==3:
        flg=ValidateArray(tmp,ary)
        if flg==True:
            sub_flg=CheckTarget(tmp,target)
            if sub_flg==True:
                fnl_lst.append(tmp.copy())
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst, target, ary)
        tmp.pop()
        cnt[i]=cnt[i]+1

def LeetCode923(ary,target):

    dict=collections.Counter(ary)
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,target,ary)
    return fnl_lst


def main():

    ary=[1,1,2,2,3,3,4,4,5,5]
    target=8
    print(LeetCode923(ary,target))

    ary =[1,1,2,2,2,2]
    target = 5
    print(LeetCode923(ary, target))

if __name__=='__main__':
    main()