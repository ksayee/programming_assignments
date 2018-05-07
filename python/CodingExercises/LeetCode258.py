'''
258. Add Digits

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Credits:
'''

def addDigits(num):
    while num > 9:
        tmp = num
        cnt = 0
        while tmp != 0:
            rem = tmp % 10
            tmp = int(tmp / 10)
            cnt = cnt + rem
        num = cnt
    return num

def main():
    num=38
    print(addDigits(num))

if __name__=='__main__':
    main()