'''
Mirror characters of a string
Given a string and a number N, we need to mirror the characters
from N-th position up to the length of the string in the alphabetical order.
In mirror operation, we change ‘a’ to ‘z’, ‘b’ to ‘y’, and so on.
Examples:
Input : N = 3
        paradox
Output : paizwlc
We mirror characters from position 3 to end.
Input : N = 6
        pneumonia
Output : pnefnlmrz

'''

def MirrorCharacterString(str1,n):

    output_list=[]
    output_list.append(str1[:n-1])
    letters='abcdefghijklmnopqrstuvwxyz'
    rev_letters=''.join(reversed(letters))

    for i in range(n-1,len(str1)):
        key=str1[i]
        idx=ord(key)-ord('a')
        output_list.append(rev_letters[idx])
    return ''.join(output_list)

def main():
    
    str1='paradox'
    n=3
    print(MirrorCharacterString(str1,n))

    str1 = 'pneumonia'
    n = 6
    print(MirrorCharacterString(str1, n))

if __name__=='__main__':
    main()