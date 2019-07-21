'''
767. Reorganize String
Medium
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
If possible, output any possible result.  If not possible, return the empty string.
Example 1:
Input: S = "aab"
Output: "aba"
Example 2:
Input: S = "aaab"
Output: ""
'''

import collections

def Validate(tmp):

    flg=True
    for i in range(1,len(tmp)):
        if tmp[i-1]==tmp[i]:
            flg=False
            break
    return flg

def Combinations_recur(lst,cnt,tmp,fnl_lst,lgt):

    if len(tmp)==lgt:
        flg=Validate(tmp)
        if flg==True:
            fnl_lst.append(''.join(tmp))
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst, lgt)
        tmp.pop()
        cnt[i]=cnt[i]+1

def LeetCode767(word):

    dict=collections.Counter(word)
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,len(word))
    return fnl_lst

def main():

    word='aab'
    print(LeetCode767(word))

    word = 'aaab'
    print(LeetCode767(word))

if __name__=='__main__':
    main()