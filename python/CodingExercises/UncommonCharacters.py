# Concatenated string with uncommon characters in Python
# Two strings are given and you have to modify 1st string such that all the common characters of the 2nd strings have to be removed and the uncommon characters of the 2nd string have to be concatenated with uncommon characters of the 1st string.

def UncommonCharacters(s1,s2):

    lst1=list(s1)
    lst2=list(s2)

    fnl_lst=[]

    for l in lst1:
        if l not in lst2:
            fnl_lst.append(l)

    for l in lst2:
        if l not in lst1:
            fnl_lst.append(l)

    return ''.join(fnl_lst)

def main():

    s1='aacdb'
    s2='gafd'
    print(UncommonCharacters(s1,s2))

    s1 = 'abcs'
    s2 = 'cxzca'
    print(UncommonCharacters(s1, s2))


if __name__=='__main__':
    main()