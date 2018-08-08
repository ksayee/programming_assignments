# Python program to check if a string is palindrome or not
# Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if reverse of the string is same as string. For example, “radar” is palindrome, but “radix” is not palindrome.
def Palindrome(str1):

    lst=list(str1)

    lst.reverse()

    if str1==''.join(lst):
        return True
    else:
        return False

def main():

    str1='malayalam'
    print(Palindrome(str1))

    str1 = 'geeks'
    print(Palindrome(str1))

    str1 = 'radar'
    print(Palindrome(str1))

    str1 = 'radix'
    print(Palindrome(str1))


if __name__=='__main__':
    main()