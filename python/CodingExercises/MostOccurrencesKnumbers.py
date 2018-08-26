# Find k numbers with most occurrences in the given array
# Given an array of n numbers and a positive integer k.
# The problem is to find k numbers with most occurrences, i.e., the top k numbers having the maximum frequency.
# If two numbers have same frequency then the larger number should be given preference.
# The numbers should be displayed in decreasing order of their frequencies.
# It is assumed that the array consists of k numbers with most occurrences.

import collections
def MostOccurrencesKnumbers(ary,k):

    dict=collections.Counter(ary)

    fnl_dict={}
    for key,val in dict.items():
        if val in fnl_dict.keys():
            fnl_dict[val].append(key)
        else:
            tmp=[]
            tmp.append(key)
            fnl_dict[val]=tmp


    sort_lst=sorted(fnl_dict.items(),key=lambda x:x[0],reverse=True)

    fnl_lst=[]
    for key,val in sort_lst:
        if key>1:
            fnl_lst.extend(sorted(val,reverse=True))
    return fnl_lst[:k]

def main():
    
    ary=[3, 1, 4, 4, 5, 2, 6, 1]
    k=2
    print(MostOccurrencesKnumbers(ary,k))

    ary = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9,10]
    k = 4
    print(MostOccurrencesKnumbers(ary, k))

if __name__=='__main__':
    main()