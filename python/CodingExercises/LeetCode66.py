'''
66. Plus One

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''


def LeetCode66(lst):

    fnl_lst=[]

    carry=1
    for i in range(len(lst)-1,-1,-1):

        sum=lst[i]+carry
        rem=sum%10
        fnl_lst.append(str(rem))
        carry=int(sum/10)
    if carry>0:
        fnl_lst.append(carry)

    fnl_lst.reverse()

    return ''.join(fnl_lst)


def main():
    
    lst=[1,2,3]
    print(LeetCode66(lst))

    lst = [4,3,2,1]
    print(LeetCode66(lst))

if __name__=='__main__':
    main()