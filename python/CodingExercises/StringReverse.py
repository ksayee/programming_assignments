# Reverse a string preserving space positions
# Write a program to Reverse the given string while preserving the position of spaces.

def StringReverse(str1):

    lst=list(str1)
    tmp=list(''.join(str1.split()))
    tmp.reverse()

    fnl_lst=[]
    i=0
    for l in lst:
        if l!=' ':
            fnl_lst.append(tmp[i])
            i=i+1
        else:
            fnl_lst.append(' ')

    return ''.join(fnl_lst)

def main():

    str1='abc de'
    print(StringReverse(str1))

    str1 = 'intern at geeks'
    print(StringReverse(str1))

    str1 = 'Help others'
    print(StringReverse(str1))

if __name__=='__main__':
    main()