'''
647. Palindromic Substrings
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''

import collections

def Validate_Palindrome(tmp):

    flg=True

    if len(tmp)==0:
        return False
    left=0
    right=len(tmp)-1

    while left<right:
        if tmp[left]!=tmp[right]:
            flg=False
            break
        left=left+1
        right=right-1

    return flg

def LeetCode647(str1):

    ary=list(str1)

    fnl_lst=[]
    tmp=[]
    lgt=len(ary)
    Combinations_recur(ary,fnl_lst,tmp,lgt)

    fnl_lst.sort()
    return fnl_lst

def Combinations_recur(ary,fnl_lst,tmp,lgt):

    if len(tmp)<=lgt:
        flg=Validate_Palindrome(tmp)
        if flg==True:
            fnl_lst.append(''.join(tmp))

    for i in range(0,len(ary)):
        tmp.append(ary[i])
        Combinations_recur(ary[i+1:], fnl_lst, tmp,lgt)
        tmp.pop()

def main():

    str1='abc'
    print(LeetCode647(str1))

    str1 = 'aaa'
    print(LeetCode647(str1))

if __name__=='__main__':
    main()