# Program to find the initials of a name.
# Given a string name. we have to find the initial of the name

def NameInitials(str1):

    lst=str1.split()
    fnl_lst=[]
    print("Full Name:",str1)
    for l in lst:
        tmp_lst=list(l)
        fnl_lst.append(tmp_lst[0].upper())

    return ' '.join(fnl_lst)

def main():

    str1='prabhat kumar singh'
    print(NameInitials(str1))

    str1 = 'Jude Law'
    print(NameInitials(str1))

    str1 = 'abhishek kumar singh'
    print(NameInitials(str1))

if __name__=='__main__':
    main()