'''
1027. Longest Arithmetic Sequence
Medium
Given an array A of integers, return the length of the longest arithmetic subsequence in A.
Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1,
and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).
Example 1:
Input: [3,6,9,12]
Output: 4
Explanation:
The whole array is an arithmetic sequence with steps of length = 3.
Example 2:
Input: [9,4,7,2,10]
Output: 3
Explanation:
The longest arithmetic subsequence is [4,7,10].
Example 3:
Input: [20,1,15,3,10,5,8]
Output: 4
Explanation:
The longest arithmetic subsequence is [20,15,10,5].
'''

import collections

def ValidateSubsequence(tmp,ary):

    idx_lst=[]

    for num in tmp:
        idx=ary.index(num)
        idx_lst.append(idx)
    if sorted(idx_lst)==idx_lst:
        return True
    else:
        return False

def ArithmeticSubsequence(tmp):

    if len(tmp)==2:
        return True
    else:
        diff=tmp[1]-tmp[0]
        for i in range(1,len(tmp)):
            int_diff=tmp[i]-tmp[i-1]
            if int_diff!=diff:
                return False
        return True

def Combinations_recur(lst,cnt,tmp,fnl_lst,ary):

    if len(tmp)>1:
        flg=ValidateSubsequence(tmp,ary)
        if flg==True:
            sub_flg=ArithmeticSubsequence(tmp)
            if sub_flg==True:
                fnl_lst.append(tmp.copy())

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst,ary)
        tmp.pop()
        cnt[i]=cnt[i]+1

def LeetCode1027(ary):

    dict=collections.Counter(ary)
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,ary)
    return sorted(fnl_lst,key=lambda x:len(x),reverse=True)[0]

def main():

    ary=[3,6,9,12]
    print(LeetCode1027(ary))

    ary = [9,4,7,2,10]
    print(LeetCode1027(ary))

    ary = [20,1,15,3,10,5,8]
    print(LeetCode1027(ary))

if __name__=='__main__':
    main()