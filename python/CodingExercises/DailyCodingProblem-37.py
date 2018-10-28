'''
This problem was asked by Google.
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
'''

import collections
def DailyCodingProblem37(ary):

    dict=collections.Counter(ary)
    lst=[]
    cnt=[]

    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    tmp=[]
    fnl_lst=[]

    Combinations_recur(lst,cnt,tmp,fnl_lst)

    return sorted(fnl_lst,key=lambda x:len(x))

def Combinations_recur(lst,cnt,tmp,fnl_lst):

    if sorted(tmp) not in fnl_lst:
        fnl_lst.append(sorted(tmp).copy())

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst)
        cnt[i]=cnt[i]+1
        tmp.pop()

def main():

    ary=[1, 2, 3]
    print(DailyCodingProblem37(ary))

if __name__=='__main__':
    main()