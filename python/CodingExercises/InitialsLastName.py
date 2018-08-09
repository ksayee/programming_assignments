# Python | Print the initials of a name with last name in full
# Given a name, print the initials of a name(uppercase) with last name(with first alphabet in uppercase) written in full separated by dots.

def InitialsLastName(s1):

    lst=s1.split()
    fnl_lst=[]

    for i in range(0,len(lst)):
        key=lst[i]
        if i==len(lst)-1:
            fnl_lst.append(key.capitalize())
        else:
            fnl_lst.append(key[0].upper())

    return '.'.join(fnl_lst)

def main():
    
    s1='geeks for geeks'
    print(InitialsLastName(s1))

    s1 = 'mohandas karamchand gandhi'
    print(InitialsLastName(s1))

if __name__=='__main__':
    main()