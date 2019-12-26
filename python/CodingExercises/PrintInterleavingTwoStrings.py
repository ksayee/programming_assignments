'''
Print all interleavings of given two strings
Given two strings str1 and str2, write a function that prints all interleavings of the given two strings.
You may assume that all characters in both strings are different
Example:

Input: str1 = "AB",  str2 = "CD"
Output:
    ABCD
    ACBD
    ACDB
    CABD
    CADB
    CDAB

Input: str1 = "AB",  str2 = "C"
Output:
    ABC
    ACB
    CAB
'''

import collections

def Validate(tmp,str1,str2):

    index_lst=[]
    for i in range(0,len(str1)):
        key=str1[i]
        idx=tmp.index(key)
        if len(index_lst)==0:
            index_lst.append(idx)
        else:
            if index_lst[-1]<idx:
                pass
            else:
                return False

    index_lst = []
    for i in range(0,len(str2)):
        key=str2[i]
        idx=tmp.index(key)
        if len(index_lst)==0:
            index_lst.append(idx)
        else:
            if index_lst[-1]<idx:
                pass
            else:
                return False
    return True

def Combinations_recur(lst,cnt,tmp,fnl_lst,str1,str2):

    if len(tmp)==len(str1+str2):
        flg=Validate(tmp,str1,str2)
        if flg==True:
            fnl_lst.append(''.join(tmp))
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst, str1, str2)
        cnt[i]=cnt[i]+1
        tmp.pop()

def PrintInterleavingTwoStrings(str1, str2):

    dict=collections.Counter(str1+str2)

    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,str1,str2)
    return fnl_lst

def main():

    str1='AB'
    str2='CD'
    print(PrintInterleavingTwoStrings(str1,str2))

    str1 = 'AB'
    str2 = 'C'
    print(PrintInterleavingTwoStrings(str1, str2))

if __name__=='__main__':
    main()