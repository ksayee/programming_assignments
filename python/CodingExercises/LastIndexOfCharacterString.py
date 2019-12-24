'''
Find last index of a character in a string
Given a string str and a character x, find last index of x in str.

Examples :

Input : str = "geeks", x = 'e'
Output : 2
Last index of 'e' in "geeks" is: 2

Input : str = "Hello world!", x = 'o'
Output : 7
Last index of 'o' is: 7

'''

def LastIndexOfCharacterString(str1, chr1):

    for i in range(len(str1)-1,-1,-1):
        key=str1[i]
        if key==chr1:
            return i
    return -1

def main():
    
    str1='geeks'
    chr1='e'
    print(LastIndexOfCharacterString(str1,chr1))

    str1 = 'Hello world!'
    chr1 = 'o'
    print(LastIndexOfCharacterString(str1, chr1))

if __name__=='__main__':
    main()