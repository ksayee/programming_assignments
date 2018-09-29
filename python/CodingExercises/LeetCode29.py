'''
29. Divide Two Integers

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
'''

def LeetCode29(dividend,divisor):

    neg_flg=False
    if dividend<0 and divisor<0:
        neg_flg=False
    elif dividend<0:
        dividend=-1*dividend
        neg_flg=True
    elif divisor<0:
        divisor=-1*divisor
        neg_flg=True

    quotient=0

    while dividend>divisor:
        quotient=quotient+1
        dividend=dividend-divisor

    if neg_flg==True:
        return (-1)*quotient
    else:
        return quotient

def main():
    
    dividend=10
    divisor=3
    print(LeetCode29(dividend,divisor))

    dividend = 7
    divisor = -3
    print(LeetCode29(dividend, divisor))

if __name__=='__main__':
    main()