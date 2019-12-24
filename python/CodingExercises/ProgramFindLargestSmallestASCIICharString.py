'''
Program to find the largest and smallest ASCII valued characters in a string
Given a string of lower case and uppercase characters, your task is to find the largest and
smallest alphabet (according to ASCII values) in the string. Note that in ASCII, all capital letters come before all small letters.
Examples :
Input : sample string
Output : Largest = t, Smallest = a

Input : Geeks
Output : Largest = s, Smallest = G
Explanation: According to alphabetical order
largest alphabet in this string is 's'
and smallest alphabet in this string is
'G'( not 'e' according to the ASCII value)

Input : geEks
Output : Largest = s, Smallest = E
'''

def ProgramFindLargestSmallestASCIICharString(str1):

    largest_chr=''
    smallest_chr=''

    for i in range(0,len(str1)):
        key=str1[i]
        if key!=' ':
            if i==0:
                largest_chr=key
                smallest_chr=key
            else:
                if ord(key)>ord(largest_chr):
                    largest_chr=key
                elif ord(key)<ord(smallest_chr):
                    smallest_chr=key
    return (largest_chr,smallest_chr)

def main():

    str1='sample string'
    print(ProgramFindLargestSmallestASCIICharString(str1))

    str1 = 'Geeks'
    print(ProgramFindLargestSmallestASCIICharString(str1))

    str1 = 'geEks'
    print(ProgramFindLargestSmallestASCIICharString(str1))

if __name__=='__main__':
    main()