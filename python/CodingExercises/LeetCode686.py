'''
686. Repeated String Match

Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
'''

def LeetCode686(A,B):

    lst1=list(A)

    flg=False
    while flg==False:

        if B not in ''.join(lst1):
            lst1.extend(list(A))
        else:
            flg=True
            break
        if len(lst1)>len(B)*2:
            break

    return flg

def main():

    A = "abcd"
    B = "cdabcdab"
    print(LeetCode686(A,B))

    A = "xyz"
    B = "cdabcdab"
    print(LeetCode686(A, B))

if __name__=='__main__':
    main()