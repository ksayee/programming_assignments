'''
6. ZigZag Conversion
Medium
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
'''

def LeetCode6(str1,numRows):

    lst=[[] for x in range(0,numRows)]

    reverseFlg=False
    k=0
    cnt=0
    for i in range(0,len(str1)):
        key=str1[i]
        if reverseFlg==True:
            j=0
            while j<cnt:
                lst[k].append(' ')
                j=j+1
            lst[k].append(key)
            if k==0:
                reverseFlg=False
                cnt=0
                k=k+1
            else:
                k=k-1
                cnt=cnt+1
        elif reverseFlg==False:
            lst[k].append(key)
            if k==numRows-1:
                k=k-1
                reverseFlg=True
            else:
                k=k+1
    for l in lst:
        print(l)

def main():

    str1='PAYPALISHIRING'
    numRows=3
    print(LeetCode6(str1,numRows))

    str1 = 'PAYPALISHIRING'
    numRows = 4
    print(LeetCode6(str1, numRows))

if __name__=='__main__':
    main()