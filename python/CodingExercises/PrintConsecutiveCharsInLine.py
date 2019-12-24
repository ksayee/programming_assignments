'''
Print consecutive characters together in a line
Given a sequence of characters, print consecutive sequence of characters in a line, otherwise
print it in a new line.
Examples:
Input  : ABCXYZACCD
Output : ABC
         XYZ
         A
         C
         CD
Input : ABCZYXACCD
Output: ABC
        ZYX
        A
        C
        CD
'''

def PrintConsecutiveCharsInLine(str1):

    tmp=[]
    tmp.append(str1[0])
    for i in range(1,len(str1)):
        prev_chr=str1[i-1]
        curr_chr=str1[i]
        if ord(prev_chr)+1==ord(curr_chr) or ord(prev_chr)-1==ord(curr_chr):
            tmp.append(curr_chr)
        else:
            print(''.join(tmp))
            tmp=[]
            tmp.append(curr_chr)
    print(''.join(tmp))

def main():

    str1='ABCXYZACCD'
    PrintConsecutiveCharsInLine(str1)

    str1 = 'ABCZYXACCD'
    PrintConsecutiveCharsInLine(str1)

if __name__=='__main__':
    main()