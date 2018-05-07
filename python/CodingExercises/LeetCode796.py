'''
796. Rotate String

We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

A and B will have length at most 100.
'''


def rotateString(A, B):
    if len(A) == 0 and len(B) == 0:
        return True

    flg = False
    i = 1
    while (i < len(A)):
        tmp = A[i:] + A[:i]
        if tmp == B:
            flg = True
            break
        else:
            i = i + 1
    return flg

def main():
    A = 'abcde'
    B = 'cdeab'
    print(rotateString(A, B))

    A = 'abcde'
    B = 'abced'
    print(rotateString(A, B))

if __name__=='__main__':
    main()