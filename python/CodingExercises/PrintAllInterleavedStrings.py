'''
Print all interleavings of given two strings
Given two strings str1 and str2, write a function that prints all interleavings of the given two strings. You may assume that all characters in both strings are different
Example:

Input: str1 = "AB",  str2 = "CD"
Output:
    ABCD
    ACBD
    ACDB
    CABD
    CADB
    CDAB

Input: str1 = "AB",  str2 = "C"
Output:
    ABC
    ACB
    CAB
'''

def printStrings_recur(str1,str2,m,n,tmp,fnl_lst,op_idx):

    if m==len(str1) and n==len(str2):
        fnl_lst.append(''.join(tmp))
        return

    if m<len(str1):
        tmp[op_idx]=str1[m]
        printStrings_recur(str1, str2, m+1, n, tmp, fnl_lst, op_idx+1)
    if n<len(str2):
        tmp[op_idx]=str2[n]
        printStrings_recur(str1, str2, m, n+1, tmp, fnl_lst, op_idx+1)

def PrintAllInterleavedStrings(str1,str2):

    m=0
    n=0
    op_idx=0
    tmp=['0']*len(str1+str2)
    fnl_lst=[]
    printStrings_recur(str1,str2,m,n,tmp,fnl_lst,op_idx)
    return fnl_lst

def main():
    
    str1='AB'
    str2='CD'
    print(PrintAllInterleavedStrings(str1,str2))

if __name__=='__main__':
    main()