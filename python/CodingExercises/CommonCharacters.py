# Given two strings, print all the common characters in lexicographical order. If there are no common letters, print -1. All letters are lower case.

def CommonCharacters(s1,s2):

    lst1=list(s1)
    lst2=list(s2)

    fnl_lst=[]

    for l in lst1:
        if l in lst2:
            idx=lst2.index(l)
            del lst2[idx]
            fnl_lst.append(l)

    return ''.join(sorted(fnl_lst))

def main():

    s1='geeks'
    s2='forgeeks'
    print(CommonCharacters(s1,s2))

    s1 = 'hhhhhello'
    s2 = 'gfghhmh'
    print(CommonCharacters(s1, s2))


if __name__=='__main__':
    main()