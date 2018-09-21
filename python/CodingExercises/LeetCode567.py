'''
567. Permutation in String
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
'''

import collections

def LeetCode567(str1, str2):

    dict=collections.Counter(str1)

    lst=[]
    cnt=[]

    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    fnl_lst=[]
    tmp=[]

    Combinations_recur(str1,str2,lst,cnt,fnl_lst,tmp)

    if len(fnl_lst)>0:
        return True
    else:
        return False

def Combinations_recur(str1,str2,lst,cnt,fnl_lst,tmp):

    if len(tmp)==len(str1):

        try:
            idx=str2.index(''.join(tmp))
        except:
            idx=-1
        if idx!=-1:
            fnl_lst.append(''.join(tmp))

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(str1, str2, lst, cnt, fnl_lst, tmp)
        tmp.pop()
        cnt[i]=cnt[i]+1



def main():

    str1='ab'
    str2='eidbaooo'
    print(LeetCode567(str1,str2))

    str1 = 'ab'
    str2 = 'eidboaoo'
    print(LeetCode567(str1, str2))


if __name__=='__main__':
    main()