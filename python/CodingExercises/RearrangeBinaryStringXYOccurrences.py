'''
Rearrange a binary string as alternate x and y occurrences
Given a binary string s and two integers x and y are given.
Task is to arrange the given string in such a way so that ‘0’ comes X-time then ‘1’
comes Y-time and so on until one of the ‘0’ or ‘1’ is finished. Then concatenate rest of the string and print the final string.
Given : x or y can not be 0
Examples:
Input : s = "0011"
        x = 1
        y = 1
Output : 0101
x is 1 and y is 1. So first we print
'0' one time the '1' one time and
then we print '0', after printing '0',
all 0's are vanished from the given
string so we concatenate rest of the
string which is '1'.
Input : s = '1011011'
        x = 1
        y = 1
Output : 0101111
'''

import collections
def RearrangeBinaryStringXYOccurrences(str1, x, y):

    dict=collections.Counter(str1)
    output_list=[]
    i=0
    flg=False
    cnt=0
    while i<len(str1):
        cnt=0
        if flg==False:
            if '0' in dict.keys():
                while cnt<x:
                    output_list.append('0')
                    dict['0'] = dict['0'] - 1
                    if dict['0'] == 0:
                        del dict['0']
                        break
                    cnt=cnt+1
                if '1' in dict.keys():
                    flg=True
        elif flg==True:
            if '1' in dict.keys():
                while cnt<x:
                    output_list.append('1')
                    dict['1'] = dict['1'] - 1
                    if dict['1'] == 0:
                        del dict['1']
                        break
                    cnt=cnt+1
                if '0' in dict.keys():
                    flg=False
        i=i+1
    return ''.join(output_list)

def main():
    
    str1="0011"
    x=1
    y=1
    print(RearrangeBinaryStringXYOccurrences(str1,x,y))

    str1 = "1011011"
    x = 1
    y = 1
    print(RearrangeBinaryStringXYOccurrences(str1, x, y))

if __name__=='__main__':
    main()