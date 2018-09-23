'''
325. Maximum Size Subarray Sum Equals k
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
'''

def LeetCode325(ary,k):

    dict={}

    curr_sum=0

    fnl_lst=[]
    for i in range(0,len(ary)):

        curr_sum=curr_sum+ary[i]

        if curr_sum==k:
            tmp=ary[0:i+1]
            fnl_lst.append(tmp.copy())
        else:
            if curr_sum in dict.keys():
                dict[curr_sum].append(i)
            else:
                tmp=[]
                tmp.append(i)
                dict[curr_sum]=tmp

        diff=curr_sum-k

        if diff in dict.keys():
            for idx in dict[diff]:
                tmp=ary[idx+1:i+1]
                fnl_lst.append(tmp.copy())

    return fnl_lst

def main():

    ary=[1, -1, 5, -2, 3]
    k=3
    print(LeetCode325(ary,k))

    ary = [-2, -1, 2, 1]
    k = 1
    print(LeetCode325(ary, k))


if __name__=='__main__':
    main()