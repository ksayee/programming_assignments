'''
784. Letter Case Permutation
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
'''

import collections
def LeetCode784(str1):

    ary=[]
    for i in range(0,len(str1)):
        key=str1[i]
        if (key>='a' and key<='z') :
            ary.append(key)
            ary.append(key.upper())
        elif (key>='A' and key<='Z'):
            ary.append(key)
            ary.append(key.lower())
        else:
            ary.append(str(key))
    dict=collections.Counter(ary)
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    fnl_lst=[]
    Combinations_recur(str1,lst,cnt,tmp,fnl_lst)
    return fnl_lst

def Combinations_recur(str1,lst,cnt,tmp,fnl_lst):

    if len(tmp)==len(str1):
        if ''.join(tmp).lower()==str1.lower():
            fnl_lst.append(''.join(tmp))

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(str1, lst, cnt, tmp, fnl_lst)
        cnt[i]=cnt[i]+1
        tmp.pop()

def main():

    str1='a1b2'
    print(LeetCode784(str1))

    str1='3z4'
    print(LeetCode784(str1))

    str1 = '12345'
    print(LeetCode784(str1))

if __name__=='__main__':
    main()