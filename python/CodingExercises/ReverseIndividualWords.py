# Reverse individual words
# Given a string str, we need to print reverse of individual words.

def ReverseIndividualWords(str1):

    lst=str1.split()
    fnl_lst=[]
    for l in lst:
        tmp=list(l)
        tmp.reverse()
        fnl_lst.append(''.join(tmp))

    return ' '.join(fnl_lst)

def main():

    str1='Hello World'
    print(ReverseIndividualWords(str1))

    str1 = 'Geeks for Geeks'
    print(ReverseIndividualWords(str1))

if __name__=='__main__':
    main()