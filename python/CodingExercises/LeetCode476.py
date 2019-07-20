'''
476. Number Complement
Easy
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.'''

def LeetCode476(num):

    lst=[]
    while num!=0:
        rem=num%2
        num=num//2
        lst.append(rem)
    lst.reverse()
    for i in range(0,len(lst)):
        key=lst[i]
        if key==1:
            lst[i]=0
        else:
            lst[i]=1

    fnl_num=0
    for i in range(len(lst)-1,-1,-1):
        fnl_num=fnl_num+lst[i]*(2**lst[i])
    return fnl_num

def main():

    num=5
    print(LeetCode476(num))

    num = 1
    print(LeetCode476(num))

if __name__=='__main__':
    main()