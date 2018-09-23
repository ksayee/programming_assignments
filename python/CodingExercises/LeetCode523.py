'''
523. Continuous Subarray Sum
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
'''

def LeetCode523(ary,k):

    dict={}

    curr_sum=0
    fnl_lst=[]
    for i in range(0,len(ary)):

        curr_sum=curr_sum+ary[i]

        if curr_sum%k==0:
            tmp=ary[0:i+1]
            fnl_lst.append(tmp.copy())
        else:
            rem=curr_sum%k

            if rem in dict.keys():
                for idx in dict[rem]:
                    tmp=ary[idx+1:i+1]
                    fnl_lst.append(tmp.copy())
                dict[rem].append(i)
            else:
                tmp=[]
                tmp.append(i)
                dict[rem]=tmp

    return fnl_lst

def main():

    ary=[23, 2, 4, 6, 7]
    k=6
    print(LeetCode523(ary,k))

    ary = [23, 2, 6, 4, 7]
    k = 6
    print(LeetCode523(ary, k))

if __name__=='__main__':
    main()