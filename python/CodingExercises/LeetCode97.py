'''
97. Interleaving String
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
'''

def LeetCode97(str1, str2, str3):
    lst1=list(str1)
    lst2=list(str2)
    lst3=list(str3)

    dp=[[False for x in range(0,len(lst1)+1)] for y in range(0,len(lst2)+1)]

    for i in range(0,len(dp)):
        for j in range(0,len(dp[0])):
            k=i+j-1
            if i==0 and j==0:
                dp[i][j]=True
            elif i==0:
                if lst1[j-1]==lst3[k]:
                    dp[i][j]=dp[i][j-1]
            elif j==0:
                if lst2[i-1]==lst3[k]:
                    dp[i][j] = dp[i-1][j]
            else:
                if lst2[i-1]==lst3[k]:
                    val1=dp[i-1][j]
                else:
                    val1=False
                if lst1[j-1]==lst3[k]:
                    val2=dp[i][j-1]
                else:
                    val2=False
                dp[i][j]=val1 | val2

    return dp[len(lst2)][len(lst1)]

def main():

    str1 = 'aab'
    str2 = 'axyz'
    str3 = 'aaxabyz'
    print(LeetCode97(str1,str2,str3))

    str1='aabcc'
    str2='dbbca'
    str3='aadbbcbcac'
    print(LeetCode97(str1,str2,str3))

    str1 = 'aabcc'
    str2 = 'dbbca'
    str3 = 'aadbbbaccc'
    print(LeetCode97(str1, str2, str3))

if __name__=='__main__':
    main()