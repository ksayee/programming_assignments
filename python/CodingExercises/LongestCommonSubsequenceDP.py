'''
Longest Common Subsequence | DP using Memoization
Given two strings s1 and s2, the task is to find the length of longest common subsequence present in both of them.
Examples:
Input: s1 = “ABCDGH”, s2 = “AEDFHR”
Output: 3
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
Input: s1 = “striver”, s2 = “raj”
Output: 1
'''

def LongestCommonSubsequence(str1,str2):

    if len(str1)>len(str2):
        big_len=len(str1)+1
        sml_len=len(str2)+1
        big_str=str1
        sml_str=str2
    else:
        big_len=len(str2)+1
        sml_len=len(str1)+1
        big_str = str2
        sml_str = str1

    lcs=[[0 for x in range(0,big_len)] for y in range(0,sml_len)]

    max_sub=0

    for i in range(1,sml_len):
        for j in range(1,big_len):
            if sml_str[i-1]==big_str[j-1]:
                lcs[i][j]=1+lcs[i-1][j-1]
            else:
                lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1])
            if lcs[i][j]>max_sub:
                max_sub=lcs[i][j]

    i=sml_len-1
    j=big_len-1

    tmp=[]
    while i>0 and j>0:
        if lcs[i][j]>0:
            num=lcs[i][j]
        if lcs[i][j-1]==num:
            j=j-1
        elif lcs[i-1][j]==num:
            i=i-1
        else:
            tmp.insert(0,big_str[j-1])
            i=i-1
            j=j-1
    print(max_sub)
    return ''.join(tmp)

def main():

    str1='BD'
    str2='ABCD'
    print(LongestCommonSubsequence(str1,str2))

    str1 = 'AGGTAB'
    str2 = 'GXTXAYB'
    print(LongestCommonSubsequence(str1, str2))

    str1 = 'striver'
    str2 = 'raj'
    print(LongestCommonSubsequence(str1, str2))


if __name__=='__main__':
    main()