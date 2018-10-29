'''
347. Top K Frequent Elements
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

import collections
def LeetCode347(ary, k):

    dict=collections.Counter(ary)

    fnl_lst=[]
    sort_dict=sorted(dict.items(),key=lambda x:x[1],reverse=True)
    for tup in sort_dict:
        fnl_lst.append(tup[0])

    return fnl_lst[:k]

def main():

    ary=[1,1,1,2,2,3]
    k=2
    print(LeetCode347(ary,k))

    ary = [1]
    k = 1
    print(LeetCode347(ary, k))

if __name__=='__main__':
    main()