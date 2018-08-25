# Majority Element
# Write a function which takes an array and prints the majority element (if it exists), otherwise prints “No Majority Element”.
# A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element).

import collections
def MajorityElement(ary):

    dict=collections.Counter(ary)
    fnl_lst=[]
    n=int(len(ary)/2)
    for key,val in dict.items():
        if val>n:
            fnl_lst.append(key)

    if len(fnl_lst)>0:
        return fnl_lst
    else:
        return "No Majority Element"

def main():
    
    ary=[3, 3, 4, 2, 4, 4, 2, 4, 4]
    print(MajorityElement(ary))

    ary = [3, 3, 4, 2, 4, 4, 2, 4]
    print(MajorityElement(ary))

if __name__=='__main__':
    main()