'''
Find Excel column number from column title
We have discussed Conversion from column number to Excel Column name. In this post, reverse is discussed.
Given a column title as appears in an Excel sheet, return its corresponding column number.

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
Examples:
Input : A
Output : 1

Input : AA
Output : 27
'''

def ExcelGivenNumbertoColumnName(word):

    output_list=[]

    num=1
    final_num=0

    for i in range(len(word)-1,-1,-1):
        key=ord(word[i])-ord('A')+1
        final_num=final_num+num*key
        num=26*num
    return final_num

def main():

    word = 'A'
    print(ExcelGivenNumbertoColumnName(word))

    word = 'AA'
    print(ExcelGivenNumbertoColumnName(word))

    word = 'Z'
    print(ExcelGivenNumbertoColumnName(word))

    word = 'AY'
    print(ExcelGivenNumbertoColumnName(word))

    word = 'AZ'
    print(ExcelGivenNumbertoColumnName(word))

    word = 'CB'
    print(ExcelGivenNumbertoColumnName(word))

    word = 'YZ'
    print(ExcelGivenNumbertoColumnName(word))

    word = 'ZZ'
    print(ExcelGivenNumbertoColumnName(word))

    word = 'AAC'
    print(ExcelGivenNumbertoColumnName(word))

if __name__=='__main__':
    main()