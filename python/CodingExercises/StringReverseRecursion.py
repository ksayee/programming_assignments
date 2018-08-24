# Print reverse of a string using recursion
# Write a recursive C function to print reverse of a given string.

def StringReverseRecursion(s,n,tmp):

    if n>=0:
        tmp.append(s[n])
        s=s[0:n]
        StringReverseRecursion(s,len(s)-1,tmp)
    return ''.join(tmp)

def main():

    str1='Geeks for Geeks'
    tmp=[]
    print(StringReverseRecursion(str1,len(str1)-1,tmp))

    str1 = 'Kartik Sayee'
    tmp = []
    print(StringReverseRecursion(str1, len(str1) - 1, tmp))

if __name__=='__main__':
    main()