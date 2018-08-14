# Remove extra spaces from a string
# Given a string containing many consecutive spaces, trim all spaces so that all words should contain only a single space between them. The conversion should be done in-place and solution should handle trailing and leading spaces and also remove preceding spaces before common punctuation like full stop, comma and a question mark.

def RemoveExtraSpaces(str):

    lst=list(str)

    tmp=[]
    fnl_lst=[]
    prev_chr=' '
    for l in lst:

        if (l>='a' and l<='z') or (l>='A' and l<='Z'):
            if prev_chr==' ':
                if len(tmp)>0:
                    fnl_lst.append(''.join(tmp))
                tmp=[]
            tmp.append(l)
        elif l==' ':
            prev_chr=' '
        else:
            tmp.append(l)
        prev_chr=l
    if len(tmp)>0:
        fnl_lst.append(''.join(tmp))

    return ' '.join(fnl_lst)

def main():

    str='   Hello Geeks . Welcome   to  GeeksforGeeks   .    '
    print(RemoveExtraSpaces(str))

    str = '  I  Love  ! ! Coding . . ! !  '
    print(RemoveExtraSpaces(str))

    str = 'GeeksforGeeks'
    print(RemoveExtraSpaces(str))

if __name__=='__main__':
    main()