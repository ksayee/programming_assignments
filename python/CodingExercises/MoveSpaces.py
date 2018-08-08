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

def main():

    str='geeks for geeks'
    print(MoveSpaces(str))

    str = 'move these spaces to beginning'
    print(MoveSpaces(str))

    str = 'Name    is   anthony   gonsalves    '
    print(MoveSpaces(str))

if __name__=='__main__':
    main()