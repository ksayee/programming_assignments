'''
This problem was asked by Palantir.
Given a number represented by a list of digits, find the next greater permutation of a
number, in terms of lexicographic ordering. If there is not greater permutation possible,
return the permutation with the lowest value/ordering.
For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should return
[2,1,3]. The list [3,2,1] should return [1,2,3].
'''

import collections
def DailyCodingProblem95(ary):

    lst=[]
    cnt=[]

    dict=collections.Counter(ary)
    sort_dict=sorted(dict.items(),key=lambda x:x[0])

    for l in sort_dict:
        key=l[0]
        val=l[1]
        lst.append(key)
        cnt.append(val)

    tmp=[]
    fnl_lst=[]
    Combinations_recur(ary,lst,cnt,tmp,fnl_lst)

    idx=fnl_lst.index(ary)
    if idx==len(fnl_lst)-1:
        return fnl_lst[0]
    else:
        return fnl_lst[idx+1]

def Combinations_recur(ary,lst,cnt,tmp,fnl_lst):

    if len(tmp)==len(ary):
        fnl_lst.append(tmp.copy())
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(ary,lst, cnt, tmp, fnl_lst)
        tmp.pop()
        cnt[i]=cnt[i]+1

def main():

    ary=[1,2,3]
    print(DailyCodingProblem95(ary))

    ary = [1,3,2]
    print(DailyCodingProblem95(ary))

    ary = [3,2,1]
    print(DailyCodingProblem95(ary))

if __name__=='__main__':
    main()