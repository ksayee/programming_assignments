def ReversingEquation(str1):

    print("Original Equation:", str1)

    lst=list(str1)
    fnl_lst=[]
    tmp=[]
    flg=False
    for i in range(len(lst)-1,-1,-1):
        key=lst[i]

        if key >='0' and key <='9':
            if flg==False:
                tmp=[]
                tmp.append(key)
                flg=True
            else:
                tmp.append(key)
        else:
            if len(tmp)>0:
                tmp.reverse()
                fnl_lst.append(''.join(tmp))
            fnl_lst.append(key)
            flg=False

    if len(tmp)>0:
        tmp.reverse()
        fnl_lst.append(''.join(tmp))

    return ''.join(fnl_lst)

def main():

    str1 = '20-30+579*29'
    print("New Equation:",ReversingEquation(str1))

    str1 = '25+39-298*11'
    print("New Equation:", ReversingEquation(str1))

    str1 = '786+1*456-6/87'
    print("New Equation:", ReversingEquation(str1))

if __name__=='__main__':
    main()