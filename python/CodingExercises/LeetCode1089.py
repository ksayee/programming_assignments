'''
1089. Duplicate Zeros
Easy
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place, do not return anything from your function.
Example 1:
Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:
Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]'''


def LeetCode1089(ary):

    i=0
    j=0
    while j<len(ary):
        if ary[i]==0:
            j=j+1
        j=j+1
        i=i+1
    i=i-1
    j=j-1
    while i>=0:
        if j<len(ary):
            ary[j]=ary[i]
        if ary[i]==0:
            j=j-1
            ary[j]=0
        i=i-1
        j=j-1
    return ary

def main():

    ary=[1,0,2,3,0,4,5,0]
    print(LeetCode1089(ary))

    ary = [1,2,3]
    print(LeetCode1089(ary))

if __name__=='__main__':
    main()