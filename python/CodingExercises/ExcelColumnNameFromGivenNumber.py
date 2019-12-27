'''
Find Excel column name from a given column number
MS Excel columns has a pattern like A, B, C, … ,Z, AA, AB, AC,…. ,AZ, BA, BB, … ZZ, AAA, AAB ….. etc. In other words, column 1 is named as “A”, column 2 as “B”, column 27 as “AA”.
Given a column number, find its corresponding Excel column name. Following are more examples.

Input          Output
 26             Z
 51             AY
 52             AZ
 80             CB
 676            YZ
 702            ZZ
 705            AAC
'''

def ExcelColumnNameFromGivenNumber(num):

    output_lst=[]

    while num>0:
        rem=(num-1)%26
        output_lst.append(chr(ord('A')+rem))
        num=(num-1)//26

    output_lst.reverse()
    return ''.join(output_lst)

def main():

    num = 26
    print(ExcelColumnNameFromGivenNumber(num))

    num = 51
    print(ExcelColumnNameFromGivenNumber(num))

    num = 52
    print(ExcelColumnNameFromGivenNumber(num))

    num = 80
    print(ExcelColumnNameFromGivenNumber(num))

    num = 676
    print(ExcelColumnNameFromGivenNumber(num))

    num = 702
    print(ExcelColumnNameFromGivenNumber(num))

    num = 705
    print(ExcelColumnNameFromGivenNumber(num))

if __name__=='__main__':
    main()