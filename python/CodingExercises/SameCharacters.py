# Quick way to check if all the characters of a string are same
# Given a string, check if all the characters of the string are same or not.

def SameCharactes(str1):

    print("String:",str1)

    if len(set(str1))==1:
        return True
    else:
        return False

def main():

    str1='geeks'
    print(SameCharactes(str1))

    str1 = 'gggg'
    print(SameCharactes(str1))

if __name__=='__main__':
    main()