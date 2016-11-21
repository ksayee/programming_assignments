
def stringreverse(str1):

    tmp=''
    for i in range(len(str1)-1,-1,-1):
        tmp=tmp+str1[i]

    return tmp

def stringreverse_rec(str1):

    if len(str1)==1:
        return str1[0]
    else:
        return str1[len(str1)-1]+stringreverse_rec(str1[0:len(str1)-1])
    
def main():
    str1='the sky is blue'
    print('Original String:', str1 )

    print('Reverse of the String:', stringreverse(str1))
    print('Reverse of the String:', stringreverse_rec(str1))


if __name__=='__main__':
    main()
