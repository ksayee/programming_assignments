'''
1053. Previous Permutation With One Swap
Medium
Given an array A of positive integers (not necessarily distinct),
return the lexicographically largest permutation that is smaller than A,
that can be made with one swap (A swap exchanges the positions of two numbers A[i] and A[j]).
If it cannot be done, then return the same array.
Example 1:
Input: [3,2,1]
Output: [3,1,2]
Explanation: Swapping 2 and 1.
Example 2:
Input: [1,1,5]
Output: [1,1,5]
Explanation: This is already the smallest permutation.
Example 3:
Input: [1,9,4,6,7]
Output: [1,7,4,6,9]
Explanation: Swapping 9 and 7.
Example 4:
Input: [3,1,1,3]
Output: [1,3,1,3]
Explanation: Swapping 1 and 3.'''

import collections

def Combinations_recur(lst,cnt,tmp,fnl_lst,lgt):

    if len(tmp)==lgt:
        if tmp not in fnl_lst:
            fnl_lst.append(tmp.copy())
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst, lgt)
        tmp.pop()
        cnt[i]=cnt[i]+1

def Validate(lst,ary):

    cnt=0

    for i in range(0,len(lst)):
        if lst[i]==ary[i]:
            pass
        else:
            cnt=cnt+1
    if cnt==2:
        return True
    else:
        return False

def LeetCode1053(ary):

    dict=collections.Counter(ary)
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,len(ary))
    fnl_lst.sort()
    idx=fnl_lst.index(ary)
    if idx==0:
        return fnl_lst[0]
    else:
        chk_lst=fnl_lst[:idx]
        for i in range(len(chk_lst)-1,-1,-1):
            flg=Validate(chk_lst[i],ary)
            if flg==True:
                return chk_lst[i]
        return ary

def main():

    ary=[3,2,1]
    print(LeetCode1053(ary))

    ary = [1,1,5]
    print(LeetCode1053(ary))

    ary = [1,9,4,6,7]
    print(LeetCode1053(ary))

    ary = [3,1,1,3]
    print(LeetCode1053(ary))

if __name__=='__main__':
    main()