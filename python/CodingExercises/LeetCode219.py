'''
219. Contains Duplicate II
Given an array of integers and an integer k,
find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

def LeetCode219(ary,k):

    for i in range(0,len(ary)):
        for j in range(i+1,len(ary)):
            if ary[i]==ary[j] and abs(i-j)<=k:
                return True

    return False


def main():

    ary=[1,2,3,1]
    k=3
    print(LeetCode219(ary,k))

    ary = [1,0,1,1]
    k = 1
    print(LeetCode219(ary,k))

    ary = [1,2,3,1,2,3]
    k = 2
    print(LeetCode219(ary,k))

if __name__=='__main__':
    main()