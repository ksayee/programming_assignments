'''
516. Longest Palindromic Subsequence
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
Example 1:
Input:
"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:
"cbbd"
Output:
2
'''

def LeetCode516(str1):

    matrix=[[0 for i in range(0,len(str1))] for j in range(0,len(str1))]

    for i in range(0,len(matrix)):
        matrix[i][i]=1

    for k in range(2,len(str1)+1):
        for i in range(0,len(str1)-k+1):
            j=i+k-1
            if i==2 and str1[i]==str1[j]:
                matrix[i][j]=2
            elif str1[i]==str1[j]:
                matrix[i][j]=matrix[i+1][j-1]+2
            else:
                matrix[i][j]=max(matrix[i+1][j],matrix[i][j-1])

    for row in matrix:
        print(row)

    return matrix[0][-1]

def main():

    str1='bbbab'
    print(LeetCode516(str1))

    str1 = 'cbbd'
    print(LeetCode516(str1))

if __name__=='__main__':
    main()