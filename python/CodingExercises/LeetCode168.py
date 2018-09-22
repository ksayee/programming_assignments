'''
168. Excel Sheet Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
'''

def LeetCode168(n):

    fnl_lst=[]

    while n>0:
        n=n-1
        rem=n%26

        fnl_lst.append(chr(ord('a')+rem))
        n=int(n/26)

    fnl_lst.reverse()

    return ''.join(fnl_lst)


def main():

    n=1
    print(LeetCode168(n))

    n = 28
    print(LeetCode168(n))

    n = 701
    print(LeetCode168(n))

if __name__=='__main__':
    main()