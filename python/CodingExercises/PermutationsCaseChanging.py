'''
Permute a string by changing case
Print all permutations of a string keeping the sequence but changing cases.
Examples:
Input : ab
Output : AB Ab ab aB
Input : ABC
Output : abc Abc aBc ABc abC AbC aBC ABC
'''

import collections

def Validate(tmp,str1):

    if ''.join(tmp).lower()==str1:
        return True
    else:
        return False

def Combinations_recur(lst,cnt,tmp,fnl_lst,str1):

    if len(tmp)==len(str1):
        flg=Validate(tmp,str1)
        if flg==True:
            fnl_lst.append(''.join(tmp))
        return
    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst, str1)
        cnt[i]=cnt[i]+1
        tmp.pop()

def PermutationsCaseChangingRecurrsion(str1):

    input=[]
    input.append(str1)
    input.append(str1.upper())
    dict=collections.Counter(''.join(input))
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,str1)
    return fnl_lst

def PermutationsCaseChanging(str1):

    lst=list(str1)
    m=1<<len(lst)
    fnl_lst=[]
    for i in range(0,m):
        tmp=lst.copy()
        for j in range(0,len(tmp)):
            if ((i>>j) & 1) == 1:
                tmp[j]=tmp[j].upper()
        fnl_lst.append(''.join(tmp))
    return fnl_lst

def main():

    str1='abc'
    print(PermutationsCaseChanging(str1))
    print(PermutationsCaseChangingRecurrsion(str1))

    str1 = 'abcd'
    print(PermutationsCaseChanging(str1))
    print(PermutationsCaseChangingRecurrsion(str1))

if __name__=='__main__':
    main()