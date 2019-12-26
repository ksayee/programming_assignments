'''
Length of longest common subsequence containing vowels
Given two strings X and Y of length m and n respectively.
The problem is to find the length of the longest common subsequence of strings X and Y which contains all vowel characters.

Examples:

Input : X = "aieef"
        Y = "klaief"
Output : aie


Input : X = "geeksforgeeks"
        Y = "feroeeks"
Output : eoee
'''

def LongestCommonSubsequenceVowels(str1,str2):

    if len(str1)>=len(str2):
        big_str=str1
        big_len=len(str1)+1
        sml_str=str2
        sml_len=len(str2)+1
    else:
        big_str = str2
        big_len = len(str2) + 1
        sml_str = str1
        sml_len = len(str1) + 1

    lst=[[0 for x in range(0,big_len)] for y in range(0,sml_len)]

    vowels=['a','e','i','o','u']
    max_sub=0
    for i in range(1,sml_len):
        for j in range(1,big_len):
            if sml_str[i-1]==big_str[j-1] and sml_str[i-1] in vowels:
                lst[i][j]=1+lst[i-1][j-1]
            else:
                lst[i][j]=max(lst[i-1][j],lst[i][j-1])
            if lst[i][j]>max_sub:
                max_sub=lst[i][j]

    i=sml_len-1
    j=big_len-1

    tmp=[]
    while i>0 and j>0:
        if lst[i][j]>0:
            num=lst[i][j]
        if num==lst[i][j-1]:
            j=j-1
        elif num==lst[i-1][j]:
            i=i=1
        else:
            tmp.insert(0,big_str[j-1])
            i=i-1
            j=j-1
    return max_sub

def main():

    str1='aieef'
    str2='klaief'
    print(LongestCommonSubsequenceVowels(str1,str2))

    str1 = 'geeksforgeeks'
    str2 = 'feroeeks'
    print(LongestCommonSubsequenceVowels(str1, str2))

if __name__=='__main__':
    main()