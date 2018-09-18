'''
357. Count Numbers with Unique Digits

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100,
             excluding 11,22,33,44,55,66,77,88,99
'''

def LeetCode357(n):

    i=0
    fnl_lst=[]
    while i<=n:

        tmp=i
        lst=[]
        flg = True
        while tmp!=0:
            rem=tmp%10
            tmp=int(tmp/10)
            if rem in lst:
                flg=False
                break
            else:
                lst.append(rem)
        if flg==True:
            fnl_lst.append(i)
        i=i+1

    return len(fnl_lst)


def main():

    n=100
    print(LeetCode357(n))

if __name__=='__main__':
    main()