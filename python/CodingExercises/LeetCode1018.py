'''
1018. Binary Prefix Divisible By 5
Easy
Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i]
interpreted as a binary number (from most-significant-bit to least-significant-bit.)
Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.
Example 1:
Input: [0,1,1]
Output: [true,false,false]
Explanation:
The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.  Only the first number is divisible by 5, so answer[0] is true.
Example 2:
Input: [1,1,1]
Output: [false,false,false]
Example 3:
Input: [0,1,1,1,1,1]
Output: [true,false,false,false,true,false]
Example 4:
Input: [1,1,1,0,1]
Output: [false,false,false,false,false]
'''

def BinaryToNumber(lst):

    sum=0
    k=0
    for i in range(len(lst)-1,-1,-1):
        sum=sum+(lst[i]*(2**k))
        k=k+1
    return sum

def LeetCode1018(ary):

    fnl_lst=[]
    for i in range(0,len(ary)):
        num=BinaryToNumber(ary[:i+1])
        if num%5==0:
            fnl_lst.append(True)
        else:
            fnl_lst.append(False)
    return fnl_lst

def main():

    ary=[0,1,1]
    print(LeetCode1018(ary))

    ary = [1,1,1]
    print(LeetCode1018(ary))

    ary = [0,1,1,1,1,1]
    print(LeetCode1018(ary))

    ary = [1,1,1,0,1]
    print(LeetCode1018(ary))

if __name__=='__main__':
    main()