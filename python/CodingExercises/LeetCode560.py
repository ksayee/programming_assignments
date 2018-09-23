'''
560. Subarray Sum Equals K
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''

def LeetCode560(ary,k):

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
            val=dict[diff]
            for idx in val:
                tmp=ary[idx+1:i+1]
                if len(tmp)>0:
                    fnl_lst.append(tmp.copy())

    return fnl_lst

def main():

    ary=[1,1,1]
    k=2
    print(LeetCode560(ary,k))

    ary = [9, 4, 20, 3, 10, 5]
    k = 33
    print(LeetCode560(ary, k))

    ary = [10, 2, -2, -20, 10]
    k = -10
    print(LeetCode560(ary, k))

    ary = [-10, 0, 2, -2, -20, 10]
    k = 20
    print(LeetCode560(ary, k))


if __name__=='__main__':
    main()