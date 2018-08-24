# Find repeated character present first in a string
# Given a string, find the repeated character present first in the string.

def FirstRepeatedChar(str):

    ary=[0]*26
    for i in range(0,len(str)):
        key=str[i]
        k=ord(key)-97
        ary[k]=ary[k]+1
        if ary[k]>1:
            return chr(k+97)
            break
    return "No repeating Character"

def main():

    str='geeksforgeeks'
    print(FirstRepeatedChar(str))

    str = 'abcdefghij'
    print(FirstRepeatedChar(str))

    str = 'abcdebjk'
    print(FirstRepeatedChar(str))

if __name__=='__main__':
    main()