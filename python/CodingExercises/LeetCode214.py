'''
214. Shortest Palindrome
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it.
Find and return the shortest palindrome you can find by performing this transformation.
Example 1:
Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:
Input: "abcd"
Output: "dcbabcd"
'''

def LeetCode214(str1):

    matrix=[['' for i in range(0,len(str1))] for j in range(0,len(str1))]

    for i in range(0,len(str1)):
        matrix[i][i]=str1[i]

    m=1
    for k in range(2,len(str1)+1):
        for i in range(0,len(str1)-k+1):
            j=i+k-1

            if str1[i]==str1[j]:
                matrix[i][j]=str1[i:j+1]
            else:
                matrix[i][j]=matrix[i+1][j][:m]+str1[i:j+1]
        m=m+1

    for row in matrix:
        print(row)

    return matrix[0][-1]

def main():

    str1 = 'abcd'
    print(LeetCode214(str1))

    str1='aacecaaa'
    print(LeetCode214(str1))

if __name__=='__main__':
    main()