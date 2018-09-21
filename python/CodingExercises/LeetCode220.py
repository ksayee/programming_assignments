'''
220. Contains Duplicate III
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
'''

def LeetCode220(ary,t,k):

    for i in range(0,len(ary)):
        for j in range(i+1,len(ary)):
            if abs(ary[i]-ary[j])<=t and abs(i-j)<=k:
                return True

    return False


def main():

    ary=[1,2,3,1]
    t=0
    k=3
    print(LeetCode220(ary,t,k))

    ary = [1,0,1,1]
    t=2
    k = 1
    print(LeetCode220(ary, t, k))

    ary = [1,5,9,1,5,9]
    t=3
    k = 2
    print(LeetCode220(ary, t, k))

if __name__=='__main__':
    main()