'''
1220. Count Vowels Permutation
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.
Example 1:
Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:
Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3:
Input: n = 5
Output: 68
'''

import collections

def Validate(tmp):

    if len(tmp)==1:
        return True

    for i in range(0,len(tmp)):

        if tmp[i]=='u':
            if i==len(tmp)-1:
                pass
            elif tmp[i+1]=='a':
                pass
            else:
                return False

        if tmp[i] == 'o':
            if i == len(tmp) - 1:
                pass
            elif tmp[i + 1] == 'i' or tmp[i+1]=='u':
                pass
            else:
                return False

        if tmp[i] == 'e':
            if i == len(tmp) - 1:
                pass
            elif tmp[i + 1] == 'a' or tmp[i+1]=='i':
                pass
            else:
                return False

        if tmp[i] == 'a':
            if i == len(tmp) - 1:
                pass
            elif tmp[i + 1] == 'e':
                pass
            else:
                return False

    return True

def Combinations_recur(lst,cnt,tmp,fnl_lst,n):

    if len(tmp)==n:
        flg=Validate(tmp)
        if flg==True:
            fnl_lst.append(''.join(tmp))
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst,n)
        cnt[i]=cnt[i]+1
        tmp.pop()

def LeetCode1220(ary,n):

    dict=collections.Counter(ary)
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,n)
    return len(fnl_lst)

def main():

    n=1
    ary=['a','e','i','o','u']
    print(LeetCode1220(ary,n))

    n = 2
    ary = ['a', 'e', 'i', 'o', 'u']
    print(LeetCode1220(ary, n))

    n = 5
    ary = ['a', 'e', 'i', 'o', 'u']
    print(LeetCode1220(ary, n))

if __name__=='__main__':
    main()