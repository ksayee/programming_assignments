'''
1312. Minimum Insertion Steps to Make a String Palindrome
Given a string s. In one step you can insert any character at any index of the string.
Return the minimum number of steps to make s palindrome.
A Palindrome String is one that reads the same backward as well as forward.
Example 1:
Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we don't need any insertions.
Example 2:
Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:
Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
Example 4:
Input: s = "g"
Output: 0
Example 5:
Input: s = "no"
Output: 1
'''

def LeetCode1312(str1):

    matrix=[['' for i in range(0,len(str1))] for j in range(0,len(str1))]

    for i in range(0,len(str1)):
        matrix[i][i]=str1[i]

    for k in range(2,len(str1)+1):
        for i in range(0,len(str1)-k+1):
            j=i+k-1
            first=str1[i]
            last=str1[j]
            if str1[i]==str1[j]:
                matrix[i][j]=first+matrix[i+1][j-1]+last
            else:
                one=first+matrix[i+1][j]+first
                two=last+matrix[i][j-1]+last
                if len(one)<len(two):
                    matrix[i][j]=one
                elif len(two)<len(one):
                    matrix[i][j]=two
                else:
                    matrix[i][j]=min(one,two)

    for row in matrix:
        print(row)

    return matrix[0][-1]

def main():

    str1='zzazz'
    print(LeetCode1312(str1))

    str1 = 'mbadm'
    print(LeetCode1312(str1))

    str1 = 'leetcode'
    print(LeetCode1312(str1))

    str1 = 'g'
    print(LeetCode1312(str1))

    str1 = 'no'
    print(LeetCode1312(str1))

if __name__=='__main__':
    main()