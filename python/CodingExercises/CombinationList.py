# Permutations of a list lst=['us','uk','in']

import collections

def CombinationList(ary):

    dict=collections.Counter(ary)

    lst=[]
    cnt=[]

    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    res=[]
    fnl_lst=[]
    CombinationList_recur(lst,cnt,res,len(ary),fnl_lst)
    return fnl_lst

def CombinationList_recur(lst,cnt,res,lgt,fnl_lst):

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        res.append(lst[i])
        fnl_lst.append(res.copy())
        cnt[i]=cnt[i]-1
        CombinationList_recur(lst, cnt, res, lgt, fnl_lst)
        res.pop()
        cnt[i]=cnt[i]+1

def main():

    ary=['us', 'uk', 'in']
    print(CombinationList(ary))

if __name__=='__main__':
    main()