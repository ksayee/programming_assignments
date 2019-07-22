'''
233. Number of Digit One
Hard
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
Example:
Input: 13
Output: 6
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
'''

def CheckOnes(n):

    while n!=0:
        rem=n%10
        if rem==1:
            return True
        n=n//10
    return False

def LeetCode233(num):

    n=1
    lst=[]
    while n<=num:
        lst.append(n)
        n=n+1
    fnl_lst=[]
    for n in lst:
        flg=CheckOnes(n)
        if flg==True:
            fnl_lst.append(n)
    return fnl_lst

def main():

    num=13
    print(LeetCode233(num))

if __name__=='__main__':
    main()