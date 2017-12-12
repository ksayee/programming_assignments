def BackwardString(str1):

    if len(str1)==1:
        return str1[0]
    else:
        return str1[len(str1)-1]+BackwardString(str1[0:len(str1)-1])

def main():

    str1='I am using hackerrank to improve programming'
    print(BackwardString(str1))

if __name__=='__main__':
    main()