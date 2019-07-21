'''
1017. Convert to Base -2
Medium
Given a number N, return a string consisting of "0"s and "1"s that represents its value in base -2 (negative two).
The returned string must have no leading zeroes, unless the string is "0".
Example 1:
Input: 2
Output: "110"
Explantion: (-2) ^ 2 + (-2) ^ 1 = 2
Example 2:
Input: 3
Output: "111"
Explantion: (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3
Example 3:
Input: 4
Output: "100"
Explantion: (-2) ^ 2 = 4
'''

def GetBinary(num):

    lst=[]
    while num!=0:
        rem=num%(-2)
        num=num//(-2)
        if rem<0:
            rem=rem+(2)
            num=num+1
        lst.append(str(rem))
    lst.reverse()
    return lst

def LeetCode1017(num):

    lst=GetBinary(num)
    return ''.join(lst)

def main():

    num=2
    print(LeetCode1017(num))

    num = 3
    print(LeetCode1017(num))

    num = 4
    print(LeetCode1017(num))

if __name__=='__main__':
    main()