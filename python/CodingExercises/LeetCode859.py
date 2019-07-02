'''
859. Buddy Strings
Easy
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.
Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false
'''

import collections

def Validate(A,B):

    lstA=list(A)
    lstB=list(B)

    com_dict=collections.Counter(A)
    diff_val_cnt=2

    for i in range(0,len(lstA)):
        if lstA[i]!=lstB[i]:
            diff_val_cnt=diff_val_cnt-1

    if diff_val_cnt==0:
        flg=True
    elif diff_val_cnt==2:
        for key,val in com_dict.items():
            if val>=2:
                flg=True
                break
            else:
                flg=False
    else:
        flg=False
    return flg

def Combinations_recur(lst,cnt,tmp,fnl_lst,B):

    if len(tmp)==len(B):
        flg=Validate(''.join(tmp),B)
        if flg==True:
            fnl_lst.append(flg)
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst, B)
        cnt[i]=cnt[i]+1
        tmp.pop()

def LeetCode859(A, B):

    if len(A)!=len(B):
        return False
    elif A==B:
        dict=collections.Counter(A)
        for key,val in dict.items():
            if val>=2:
                return True
        return False
    else:
        dict=collections.Counter(A)
        lst=[]
        cnt=[]
        for key,val in dict.items():
            lst.append(key)
            cnt.append(val)

        tmp=[]
        fnl_lst=[]
        Combinations_recur(lst,cnt,tmp,fnl_lst,B)

        if len(fnl_lst)>0:
            return True
        else:
            return False

def main():

    A = "ab"
    B = "ba"
    print(LeetCode859(A,B))

    A = "ab"
    B = "ab"
    print(LeetCode859(A, B))

    A = "aa"
    B = "aa"
    print(LeetCode859(A, B))

    A = "aaaaaaabc"
    B = "aaaaaaacb"
    print(LeetCode859(A, B))

    A = ""
    B = "aa"
    print(LeetCode859(A, B))

if __name__=='__main__':
    main()