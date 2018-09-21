'''
229. Majority Element II
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
'''

import collections

def LeetCode229(ary):

    dict=collections.Counter(ary)

    fnl_lst=[]

    for key,val in dict.items():
        if val>int(len(ary)/3):
            fnl_lst.append(key)

    return fnl_lst

def main():

    ary=[3,2,3]
    print(LeetCode229(ary))

    ary = [1,1,1,3,3,2,2,2]
    print(LeetCode229(ary))

if __name__=='__main__':
    main()