# Python code to move spaces to front of string in single traversal
# Given a string that has set of words and spaces, write a program to move all spaces to front of string, by traversing the string only once.

def MoveSpaces(str):

    lst=str.split()
    fnl_lst=[]

    for i in range(0,len(str)):
        key=str[i]

        if key==' ':
            fnl_lst.append(key)

    return ''.join(fnl_lst)+''.join(lst)

def MoveSpacesIter(str):

    fnl_lst=[]
    spc_lst=[]
    tmp=[]

    flg=False
    for i in range(0,len(str)):
        key=str[i]
        if key!=' ':
            if flg==False:
                tmp.append(key)
                flg=True
            else:
                tmp.append(key)
        else:
            if len(tmp) > 0:
                fnl_lst.append(''.join(tmp))
                tmp=[]
            spc_lst.append(key)
            flg=False
    if len(tmp)>0:
        fnl_lst.append(''.join(tmp))

    return ''.join(spc_lst)+''.join(fnl_lst)

def main():

    str='geeks for geeks'
    print(MoveSpaces(str))
    print(MoveSpacesIter(str))

    str = 'move these spaces to beginning'
    print(MoveSpaces(str))
    print(MoveSpacesIter(str))

    str = 'Name    is   anthony   gonsalves    '
    print(MoveSpaces(str))
    print(MoveSpacesIter(str))

if __name__=='__main__':
    main()