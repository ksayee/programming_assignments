'''
336. Palindrome Pairs
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
'''

import collections

def Validate_palindrom(str1):

    lst=list(str1)
    flg=True

    left=0
    right=len(lst)-1

    while left<right:
        if lst[left]==lst[right]:
            left=left+1
            right=right-1
        else:
            flg=False
            break
    return flg

def LeetCode336(ary):

    dict=collections.Counter(ary)

    lst=[]
    cnt=[]
    for key,val in dict.items():

        lst.append(key)
        cnt.append(val)

    fnl_lst={}
    tmp=[]

    Combinations_recur(lst,cnt,fnl_lst,tmp,ary)

    return fnl_lst

def Combinations_recur(lst,cnt,fnl_lst,tmp,ary):

    if len(tmp)==2:
        flg=Validate_palindrom(''.join(tmp))
        if flg==True:
            idx1=ary.index(tmp[0])
            idx2=ary.index(tmp[1])
            if ''.join(tmp) not in fnl_lst.keys():
                tmp_lst=[]
                tup=(idx1,idx2)
                tmp_lst.append(tup)
                fnl_lst[''.join(tmp)]=tmp_lst
            else:
                tup=(idx1,idx2)
                fnl_lst[''.join(tmp)].append(tup)


    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, fnl_lst, tmp, ary)
        tmp.pop()
        cnt[i]=cnt[i]+1

def main():

    ary=["abcd","dcba","lls","s","sssll"]
    print(LeetCode336(ary))

    ary = ["bat","tab","cat"]
    print(LeetCode336(ary))

if __name__=='__main__':
    main()