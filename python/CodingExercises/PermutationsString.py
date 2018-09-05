# Permutations of a string aabc

import collections

def permutation(str1):

    dict=collections.Counter(str1)

    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    res=[]

    fnl_lst=[]
    permutation_recur(lst,cnt,res,len(str1),fnl_lst)

    return fnl_lst

def permutation_recur(lst,cnt,res,lgt,fnl_lst):

    if len(res)==lgt:
        fnl_lst.append(''.join(res))

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        res.append(lst[i])
        cnt[i]=cnt[i]-1
        permutation_recur(lst, cnt, res,lgt, fnl_lst)
        res.pop()
        cnt[i]=cnt[i]+1

def main():

    str1='aabc'
    print(permutation(str1))

if __name__=='__main__':
    main()