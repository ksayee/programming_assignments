# Minimum operation to make all elements equal in array
# Given an array with n positive integers.
# We need to find the minimum number of operation to make all elements equal.
# We can perform addition, multiplication, subtraction or division with any element on an array element.

import collections

def MinimumOperationsArrayEqual(ary):

    dict=collections.Counter(ary)

    sort_lst=sorted(dict.items(),key=lambda x:x[1],reverse=True)

    return len(ary)-sort_lst[0][1]

def main():
    
    ary=[1, 2, 3, 4]
    print(MinimumOperationsArrayEqual(ary))

    ary = [1, 1, 1, 1]
    print(MinimumOperationsArrayEqual(ary))

if __name__=='__main__':
    main()