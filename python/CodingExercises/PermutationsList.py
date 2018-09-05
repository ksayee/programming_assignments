# Permutations of a list lst=['us','uk','in']

import collections

def PermutationsList(ary):

    dict=collections.Counter(ary)

    lst=[]
    cnt=[]

    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    res=[]
    fnl_lst=[]
    PermutationsList_recur(lst,cnt,res,len(ary),fnl_lst)
    return fnl_lst

def PermutationsList_recur(lst,cnt,res,lgt,fnl_lst):

    if len(res)==lgt:
        fnl_lst.append(res.copy())

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        res.append(lst[i])
        cnt[i]=cnt[i]-1
        PermutationsList_recur(lst, cnt, res, lgt, fnl_lst)
        res.pop()
        cnt[i]=cnt[i]+1

def main():

    ary=['us', 'uk', 'in']
    print(PermutationsList(ary))

if __name__=='__main__':
    main()