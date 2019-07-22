'''
828. Unique Letter String
Hard
A character is unique in string S if it occurs exactly once in it.
For example, in string S = "LETTER", the only unique characters are "L" and "R".
Let's define UNIQ(S) as the number of unique characters in string S.
For example, UNIQ("LETTER") =  2.
Given a string S with only uppercases, calculate the sum of UNIQ(substring) over all non-empty substrings of S.
If there are two or more equal substrings at different positions in S, we consider them different.
Since the answer can be very large, return the answer modulo 10 ^ 9 + 7.
Example 1:
Input: "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Evey substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
Example 2:
Input: "ABA"
Output: 8
Explanation: The same as example 1, except uni("ABA") = 1.
'''

import collections
def CollateSubstrings(sub_string,fnl_lst):

    lst=sub_string.split(',')
    for check in lst:
        if check not in fnl_lst:
            fnl_lst.append(check)

def Combinations_recur(idx,op_idx,tmp,fnl_lst,word):

    if idx==len(word):
        CollateSubstrings(''.join(tmp).strip(','),fnl_lst)
        return

    tmp[op_idx]=word[idx]
    tmp[op_idx+1]=','
    Combinations_recur(idx+1, op_idx+2, tmp, fnl_lst,word)

    if idx+1<len(word):
        Combinations_recur(idx+1, op_idx+1, tmp, fnl_lst,word)

def LeetCode828(word):

    tmp=[0]*(2*len(word))
    idx=0
    op_idx=0
    fnl_lst=[]
    Combinations_recur(idx,op_idx,tmp,fnl_lst,word)

    cnt=0
    for sub in fnl_lst:
        dict=collections.Counter(sub)
        for key,val in dict.items():
            if val==1:
                cnt=cnt+1
    return cnt

def main():

    word='ABC'
    print(LeetCode828(word))

    word = 'ABA'
    print(LeetCode828(word))

if __name__=='__main__':
    main()