# Check if all occurrences of a character appear together
# Given a string s and a character c, find if all occurrences of c appear together in s or not. If the character c does not appear in the string at all, the answer is true.

def OccurencesCharTogether(ary,c):

    lst=list(ary)
    seenFlg=False
    for i in range(0,len(lst)):
        key=lst[i]
        if key==c:
            seenFlg=True
        else:
            if seenFlg==True:
                if c not in lst[i+1:]:
                    return True
                else:
                    return False

    return seenFlg

def main():

    str='1110000323'
    c='1'
    print(OccurencesCharTogether(str,c))

    str = '3231131'
    c = '1'
    print(OccurencesCharTogether(str, c))


    str = 'abcabc'
    c = 'c'
    print(OccurencesCharTogether(str, c))

    str = 'ababcc'
    c = 'c'
    print(OccurencesCharTogether(str, c))

if __name__=='__main__':
    main()