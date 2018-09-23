'''
643. Maximum Average Subarray I
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
'''

def LeetCode643(ary,k):

    curr_sum=0
    for i in range(0,len(ary)):

        if i<k:
            curr_sum=curr_sum+ary[i]
        else:
            break

    tmp=[0,k]
    max_val=curr_sum
    for i in range(k,len(ary)):

        curr_sum=curr_sum+ary[i]-ary[i-k]
        if curr_sum>max_val:
            max_val=curr_sum
            tmp=[i-k+1,i+1]

    return ary[tmp[0]:tmp[1]]

def main():

    ary=[1,12,-5,-6,50,3]
    k=4
    print(LeetCode643(ary,k))

    ary=[3, 7, 90, 20, 10, 50, 40]
    k=3
    print(LeetCode643(ary,k))

    ary=[3, 7, 5, 20, -10, 0, 12]
    k=2
    print(LeetCode643(ary,k))

if __name__=='__main__':
    main()