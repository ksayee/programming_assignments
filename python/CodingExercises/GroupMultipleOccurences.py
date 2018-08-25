# Group multiple occurrence of array elements ordered by first occurrence
# Given an unsorted array with repetitions,
# the task is to group multiple occurrence of individual elements.
# The grouping should happen in a way that the order of first occurrences of all elements is maintained.

import collections
def GroupMultipleOccurences(ary):

    dict=collections.Counter(ary)

    dst=set(ary)

    lst=[]
    for k in dst:
        idx=ary.index(k)
        lst.append(idx)
    lst_sort=sorted(lst)

    fnl_lst=[]
    for l in lst_sort:
        key=ary[l]

        val=dict[key]

        n=0
        while n<val:
            fnl_lst.append(key)
            n=n+1
    return fnl_lst
    
def main():
    
    ary=[5, 3, 5, 1, 3, 3]
    print(GroupMultipleOccurences(ary))

    ary = [4, 6, 9, 2, 3, 4, 9, 6, 10, 4]
    print(GroupMultipleOccurences(ary))

if __name__=='__main__':
    main()