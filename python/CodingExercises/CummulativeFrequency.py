# Cumulative frequency of count of each element in an unsorted array
# Given an unsorted array.
# The task is to calculate the cumulative frequency of each element of the array using count array.

import collections
def CummulativeFrequency(ary):

    dict=collections.Counter(ary)

    dst=set(ary)
    lst=[]
    for l in dst:
        idx=ary.index(l)
        lst.append(idx)

    lst_sort=sorted(lst)

    fnl_lst=[]

    cum_sum=0
    for k in lst_sort:
        key=ary[k]

        val=dict[key]
        cum_sum=cum_sum+val
        tup=(key,cum_sum)
        fnl_lst.append(tup)

    return fnl_lst
    
def main():
    
    ary=[1, 2, 2, 1, 3, 4]
    print(CummulativeFrequency(ary))

    ary = [1, 1, 1, 2, 2, 2]
    print(CummulativeFrequency(ary))

if __name__=='__main__':
    main()