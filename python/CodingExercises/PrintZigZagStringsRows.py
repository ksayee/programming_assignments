'''
Print Concatenation of Zig-Zag String in ‘n’ Rows
Given a string and number of rows ‘n’.
Print the string formed by concatenating n rows when input string is written in row-wise Zig-Zag fashion.
Examples:
Input: str = "ABCDEFGH"
       n = 2
Output: "ACEGBDFH"
Explanation: Let us write input string in Zig-Zag fashion
             in 2 rows.
A   C   E   G
  B   D   F   H
Now concatenate the two rows and ignore spaces
in every row. We get "ACEGBDFH"

Input: str = "GEEKSFORGEEKS"
       n = 3
Output: GSGSEKFREKEOE
Explanation: Let us write input string in Zig-Zag fashion
             in 3 rows.
G       S       G       S
  E   K   F   R   E   K
    E       O       E
Now concatenate the two rows and ignore spaces
in every row. We get "GSGSEKFREKEOE"
'''

def PrintZigZagStringsRows(str1,n):

    lst=[]
    for i in range(0,n):
        tmp=[' ']*len(str1)
        lst.append(tmp.copy())
    k=0
    flg=True
    for i in range(0,len(str1)):
        key=str1[i]

        if flg==True:
            lst[k][i]=key
            if k==n-1:
                flg=False
                k=k-1
            else:
                k=k+1
        else:
            lst[k][i]=key
            if k==0:
                flg=True
                k=k+1
            else:
                k=k-1

    for tup in lst:
        print(''.join(tup))

def main():

    str1='ABCDEFGH'
    n=2
    PrintZigZagStringsRows(str1,n)

    str1 = 'GEEKSFORGEEKS'
    n=3
    PrintZigZagStringsRows(str1,n)

if __name__=='__main__':
    main()