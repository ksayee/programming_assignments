# In-place replace multiple occurrences of a pattern
# Given a string and a pattern, replace multiple occurrences of a pattern by character ‘X’.
# The conversion should be in-place and solution should replace multiple consecutive (and non-overlapping) occurrences of a pattern by a single ‘X’.

def ReplaceMultipleOccurencesPattern(str1, ptrn):

    ptrn_lst=list(ptrn)

    lst=list(str1)
    flg=False
    tmp=[]
    i=0
    fnl_lst=[]
    for l in lst:
        if flg==False and l==ptrn_lst[i]:
            flg=True
            tmp.append(l)
            i=i+1
        elif flg==True and l==ptrn_lst[i]:
            tmp.append(l)
            i=i+1
        elif flg==True:
            if l!=ptrn_lst[i]:
                flg=False
                i=0
                fnl_lst.extend(tmp)
                tmp=[]
        if flg==True:
            if ''.join(tmp)==ptrn:
                if len(fnl_lst)==0:
                    fnl_lst.append('X')
                elif fnl_lst[-1]=='X':
                    i = 0
                    tmp = []
                    flg = False
                else:
                    fnl_lst.append('X')
                i=0
                tmp=[]
                flg=False
        else:
            fnl_lst.append(l)
    fnl_lst.extend(tmp)
    return ''.join(fnl_lst)

def main():

    str1='GeeksForGeeks'
    ptrn='Geeks'
    print(ReplaceMultipleOccurencesPattern(str1,ptrn))

    str1 = 'GeeksGeeks'
    ptrn = 'Geeks'
    print(ReplaceMultipleOccurencesPattern(str1, ptrn))

    str1 = 'GeeSayGeeksGeeks'
    ptrn = 'Geeks'
    print(ReplaceMultipleOccurencesPattern(str1, ptrn))

    str1 = 'aaaa'
    ptrn = 'aa'
    print(ReplaceMultipleOccurencesPattern(str1, ptrn))

    str1 = 'aaaaTestaa'
    ptrn = 'aa'
    print(ReplaceMultipleOccurencesPattern(str1, ptrn))

    str1 = 'aaaaa'
    ptrn = 'aa'
    print(ReplaceMultipleOccurencesPattern(str1, ptrn))

if __name__=='__main__':
    main()