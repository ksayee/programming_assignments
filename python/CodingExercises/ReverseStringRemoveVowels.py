# Print reverse string after removing vowels
# Given a string s, print reverse of string and remove the characters from the reversed string where there are vowels in the original string.

def ReverseStringRemoveVowels(str1):

    vow=['a','e','i','o','u']

    lst=list(str1)

    lst.reverse()

    for i in range(0,len(str1)):
        key=str1[i]

        if key in vow:
            lst[i]=''

    return ''.join(lst)

def main():

    str1='geeksforgeeks'
    print(ReverseStringRemoveVowels(str1))

    str1 = 'duck'
    print(ReverseStringRemoveVowels(str1))

if __name__=='__main__':
    main()