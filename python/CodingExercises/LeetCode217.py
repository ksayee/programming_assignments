'''
21. Conta7ins Duplicate
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
Example 1:
Input: [1,2,3,1]
Output: true
Example 2:
Input: [1,2,3,4]
Output: false
Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

import collections

def LeetCode217(ary):

    flg=False

    for i in range(0,len(ary)):
        key=ary[i]
        if key in ary[:i] or key in ary[i+1:]:
            flg=True
            break
    return flg


def main():

    ary=[1,2,3,1]
    print(LeetCode217(ary))

    ary = [1,2,3,4]
    print(LeetCode217(ary))

    ary = [1,1,1,3,3,4,3,2,4,2]
    print(LeetCode217(ary))

if __name__=='__main__':
    main()