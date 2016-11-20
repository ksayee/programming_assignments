
def stringreverse(str1):

    tmp=''
    for i in range(len(str1)-1,-1,-1):
        tmp=tmp+str1[i]

    return tmp

def main():
    str1='My name is Kartik Sayee'
    print('Original String:', str1 )

    print('Reverse of the String:', stringreverse(str1))



if __name__=='__main__':
    main()
