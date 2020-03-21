'''
1296. Divide Array in Sets of K Consecutive Numbers
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.
Example 1:
Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
Example 2:
Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
Example 3:
Input: nums = [3,3,2,2,1,1], k = 3
Output: true
Example 4:
Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.
'''

def LeetCode1296(ary, k):

    ary_size=len(ary)
    ary.sort()
    output_lst=[]
    cnt=1
    tmp=[]
    tmp.append(ary[0])
    ary.pop(0)
    while True:
        if cnt==k:
            if len(ary)==0:
                output_lst.append(tmp.copy())
                break
            else:
                output_lst.append(tmp.copy())
                cnt=1
                tmp=[]
                tmp.append(ary[0])
                ary.pop(0)
        next_num=tmp[-1]+1
        try:
            idx=ary.index(next_num)
            tmp.append(ary[idx])
            cnt=cnt+1
            ary.pop(idx)
        except:
            return ([],False)
    return (output_lst,True)

def main():

    ary=[1,2,3,3,4,4,5,6]
    k=4
    print(LeetCode1296(ary,k))

    ary = [3,2,1,2,3,4,3,4,5,9,10,11]
    k = 3
    print(LeetCode1296(ary, k))

    ary = [3,3,2,2,1,1]
    k = 3
    print(LeetCode1296(ary, k))

    ary = [1,2,3,4]
    k = 3
    print(LeetCode1296(ary, k))


if __name__=='__main__':
    main()