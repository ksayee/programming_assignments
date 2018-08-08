# Check if both halves of the string have same set of characters in Python
# Given a string of lowercase characters only, the task is to check if it is possible to split a string from middle which will gives two halves having the same characters and same frequency of each character. If the length of the given string is ODD then ignore the middle element and check for the rest.

def BothHalves(s1):

    lst=list(s1)
    if len(lst)%2==0:
        lst1=lst[0:int(len(lst)/2)]
        lst2 = lst[int(len(lst) / 2):]
    else:
        lst1 = lst[0:int(len(lst) / 2)]
        lst2 = lst[int(len(lst)/ 2)+1:]

    print(lst1,lst2)
    if ''.join(sorted(lst1))==''.join(sorted(lst2)):
        return True
    else:
        return False

def main():

    s1='abbaab'
    print(BothHalves(s1))

    s1 = 'abccab'
    print(BothHalves(s1))

    s1 = 'abcaabc'
    print(BothHalves(s1))


if __name__=='__main__':
    main()