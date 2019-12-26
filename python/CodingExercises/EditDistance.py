'''
Edit distance and LCS (Longest Common Subsequence)
In standard Edit Distance where we are allowed 3 operations, insert, delete and replace.
Consider a variation of edit distance where we are allowed only two operations insert and delete, find edit distance in this variation.
Examples:
Input : str1 = "cat", st2 = "cut"
Output : 2
We are allowed to insert and delete. We delete 'a'
from "cat" and insert "u" to make it "cut".

Input : str1 = "acb", st2 = "ab"
Output : 1
We can convert "acb" to "ab" by removing 'c'.
Recommended: Please try your approach on {IDE} first, before moving on to the solution.
One solution is to simply modify Edit Distance Solution by making two recursive call instead of three. An interesting solution is based on LCS.
1) Find LCS of two strings. Let length of LCS be x.
2) Let length of first string be m and length of second string be n. Our result is (m – x) + (n – x). We basically need to do (m – x) delete operations and (n – x) insert operations.
'''

def GetLongestCommonSubsequence(lst,big_str,big_num,sml_str,sml_num):

    max_sub=0
    for i in range(1,sml_num):
        for j in range(1,big_num):
            if sml_str[i-1]==big_str[j-1]:
                lst[i][j]=1+lst[i-1][j-1]
            else:
                lst[i][j]=max(lst[i-1][j],lst[i][j-1])
            if lst[i][j]>max_sub:
                max_sub=lst[i][j]
    tmp=[]

    i=sml_num-1
    j=big_num-1

    while i>0 and j>0:
        if lst[i][j]>0:
            num=lst[i][j]
        if num==lst[i-1][j]:
            i=i-1
        elif num==lst[i][j-1]:
            j=j-1
        else:
            tmp.insert(0,big_str[j-1])
            i=i-1
            j=j-1
    return (max_sub,''.join(tmp))

def EditDistance(str1,str2):

    if len(str1)>=len(str2):
        big_str=str1
        big_num=len(str1)+1
        sml_str = str2
        sml_num = len(str2) + 1
    else:
        big_str = str2
        big_num = len(str2) + 1
        sml_str = str1
        sml_num = len(str1) + 1

    lst=[[0 for x in range(0,big_num)] for y in range(0,sml_num)]

    tup=GetLongestCommonSubsequence(lst,big_str,big_num,sml_str,sml_num)
    return (len(str1)-tup[0])+(len(str2)-tup[0])

def main():

    str1='cat'
    str2='cut'
    print(EditDistance(str1,str2))

    str1 = 'acb'
    str2 = 'ab'
    print(EditDistance(str1, str2))


if __name__=='__main__':
    main()