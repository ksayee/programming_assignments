'''
442. Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
'''

import collections

def LeetCode442(ary):

    dict=collections.Counter(ary)

    fnl_lst=[]

    for key,val in dict.items():
        if val==2:
            fnl_lst.append(key)

    return fnl_lst

def main():

    ary=[4,3,2,7,8,2,3,1]
    print(LeetCode442(ary))

if __name__=='__main__':
    main()