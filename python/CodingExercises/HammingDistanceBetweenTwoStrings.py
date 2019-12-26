'''
Hamming Distance between two strings

You are given two strings of equal length, you have to find the Hamming Distance between these string.
Where the Hamming distance between two strings of equal length is the number of positions at which the corresponding character are different.

Examples:

Input : str1[] = "geeksforgeeks", str2[] = "geeksandgeeks"
Output : 3
Explanation : The corresponding character mismatch are highlighted.
"geeksforgeeks" and "geeksandgeeks"

Input : str1[] = "1011101", str2[] = "1001001"
Output : 2
Explanation : The corresponding character mismatch are highlighted.
"1011101" and "1001001"
'''

def HammingDistanceBetweenTwoStrings(str1,str2):

    count=0
    for i in range(0,len(str1)):
        if str1[i]!=str2[i]:
            count=count+1
    return count


def main():

    str1='geeksforgeeks'
    str2='geeksandgeeks'
    print(HammingDistanceBetweenTwoStrings(str1,str2))

    str1 = '1011101'
    str2 = '1001001'
    print(HammingDistanceBetweenTwoStrings(str1, str2))

if __name__=='__main__':
    main()