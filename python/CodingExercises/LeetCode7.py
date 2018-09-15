'''
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

'''


def LeetCode7(n):

    if n<0:
        n=(-1)*n
        flg=True
    else:
        flg=False

    zero_flg=True
    fnl_lst=[]
    while n!=0:
        rem=n%10
        if rem==0 and zero_flg==True:
            n=int(n/10)
        else:
            if zero_flg==True:
                zero_flg=False
            fnl_lst.append(str(rem))
            n = int(n / 10)

    if flg==True:
        return (-1)*int(''.join(fnl_lst))
    else:
        return int(''.join(fnl_lst))

def main():
    
    n=123
    print(LeetCode7(n))

    n = -123
    print(LeetCode7(n))

    n = 120
    print(LeetCode7(n))

    n = -500400
    print(LeetCode7(n))

if __name__=='__main__':
    main()