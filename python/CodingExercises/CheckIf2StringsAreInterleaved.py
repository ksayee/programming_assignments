# Program to check if input is an integer or a string
# Write a function to check whether a given input is an integer or a string.

def CheckInterleaved_recur(str1,str2,target,m,n,k):

    if m==len(str1) and n==len(str2) and k==len(target):
        return True
    if k==len(target):
        return False

    if m<len(str1) and str1[m]==target[k]:
        return CheckInterleaved_recur(str1, str2, target, m+1, n, k+1)
    if n<len(str2) and str2[n]==target[k]:
        return CheckInterleaved_recur(str1,str2,target,m,n+1,k+1)
    return False

def CheckifTwoStringsInterleaved(str1,str2,target):

    m=0
    n=0
    k=0
    return CheckInterleaved_recur(str1,str2,target,m,n,k)

def main():

    str1 = 'ABC'
    str2 = 'DEF'
    target = 'ADEBCF'
    print(CheckifTwoStringsInterleaved(str1, str2, target))

    str1='aabcc'
    str2='dbbca'
    target='aadbbcbcac'
    print(CheckifTwoStringsInterleaved(str1,str2,target))

    str1 = 'aab'
    str2 = 'axy'
    target = 'abaaxy'
    print(CheckifTwoStringsInterleaved(str1, str2, target))

    str1 = 'XXY'
    str2 = 'XXZ'
    target = 'XXZXXXY'
    print(CheckifTwoStringsInterleaved(str1, str2, target))

    str1 = 'XY'
    str2 = 'WZ'
    target = 'WZXY'
    print(CheckifTwoStringsInterleaved(str1, str2, target))

    str1 = 'XY'
    str2 = 'X'
    target = 'XXY'
    print(CheckifTwoStringsInterleaved(str1, str2, target))

    str1 = 'YX'
    str2 = 'X'
    target = 'XXY'
    print(CheckifTwoStringsInterleaved(str1, str2, target))

    str1 = 'XXY'
    str2 = 'XXZ'
    target = 'XXXXZY'
    print(CheckifTwoStringsInterleaved(str1, str2, target))

if __name__=='__main__':
    main()