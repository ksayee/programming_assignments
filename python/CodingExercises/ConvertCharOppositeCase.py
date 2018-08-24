# Convert characters of a string to opposite case
# Given a string, convert the characters of the string into opposite case,i.e. if a character is lower case than convert it into upper case and vice-versa.

def ConvertCharOppositeCase(str1):

    fnl_lst=[]

    for i in range(0,len(str1)):
        key=str1[i]

        if key>='A' and key<='Z':
            fnl_lst.append(key.lower())
        else:
            fnl_lst.append(key.upper())

    return ''.join(fnl_lst)

def main():

    str1='geeksForgEeks'
    print(ConvertCharOppositeCase(str1))

    str1 = 'hello every one'
    print(ConvertCharOppositeCase(str1))

if __name__=='__main__':
    main()