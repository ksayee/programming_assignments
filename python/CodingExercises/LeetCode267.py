'''
267. Palindrome Permutation II
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]
Example 2:

Input: "abc"
Output: []
'''

import collections

def Validated_Palindrome(str1):

    lst=list(str1)

    left=0
    right=len(lst)-1

    flg=True
    while left<right:

        if lst[left]==lst[right]:
            left=left+1
            right=right-1
        else:
            flg=False
            break

    return flg

def LeetCode267(str1):

    dict=collections.Counter(str1)

    lst=[]
    cnt=[]

    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    fnl_lst=[]
    tmp=[]
    lgt=len(str1)
    Combinations_recur(lst,cnt,fnl_lst,tmp,lgt)

    return fnl_lst

def Combinations_recur(lst,cnt,fnl_lst,tmp,lgt):

    if len(tmp)==lgt:
        flg=Validated_Palindrome(''.join(tmp))
        if flg==True:
            fnl_lst.append(''.join(tmp))

    for i in range(0,len(lst)):

        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, fnl_lst, tmp,lgt)
        tmp.pop()
        cnt[i]=cnt[i]+1

def main():

    str1='aabb'
    print(LeetCode267(str1))

    str1 = 'abc'
    print(LeetCode267(str1))

if __name__=='__main__':
    main()