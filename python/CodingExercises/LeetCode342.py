'''
342. Power of Four
Easy
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
Example 1:
Input: 16
Output: true
Example 2:
Input: 5
Output: false
'''

def LeetCode342(num):

    flg=True
    while num!=1:
        if num%4!=0:
            flg=False
            break
        num=num//4
    return flg

def main():

    num=16
    print(LeetCode342(num))

    num = 5
    print(LeetCode342(num))

if __name__=='__main__':
    main()