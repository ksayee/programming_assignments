'''
260. Single Number III
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
'''

import collections

def LeetCode260(ary):

    dict=collections.Counter(ary)

    fnl_lst=[]
    for key,val in dict.items():
        if val==1:
            fnl_lst.append(key)
    return fnl_lst

def main():

    ary=[1,2,1,3,2,5]
    print(LeetCode260(ary))

if __name__=='__main__':
    main()