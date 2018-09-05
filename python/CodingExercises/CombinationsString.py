# Permutations of a string aabc

import collections

def combination(str1):

    dict=collections.Counter(str1)
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    res=[]
    fnl_lst=[]
    combination_recur(lst,cnt,res,fnl_lst)
    return fnl_lst

def combination_recur(lst,cnt,res,fnl_lst):

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        res.append(lst[i])
        fnl_lst.append(''.join(res))
        cnt[i]=cnt[i]-1
        combination_recur(lst, cnt, res, fnl_lst)
        res.pop()
        cnt[i]=cnt[i]+1
    return

def main():

    str1='abc'
    print(combination(str1))

if __name__=='__main__':
    main()