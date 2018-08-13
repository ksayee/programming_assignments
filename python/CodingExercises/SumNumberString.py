# Calculate sum of all numbers present in a string
# Given a string containing alphanumeric characters, calculate sum of all numbers present in the string.

def SumNumberString(str):

    lst=list(str)

    flg=False
    sum=0
    tmp=[]

    for l in lst:

        if l >='0' and l <= '9':
            tmp.append(l)
            flg=True
        else:
            if len(tmp)>0:
                sum = sum + int(''.join(tmp))
            tmp=[]
            flg=False

    if flg==True:
        sum = sum + int(''.join(tmp))
    return sum

def main():
    
    str='1abc23'
    print(SumNumberString(str))

    str = 'geeks4geeks'
    print(SumNumberString(str))

    str = '1abc2x30yz67'
    print(SumNumberString(str))

    str = '123abc'
    print(SumNumberString(str))

if __name__=='__main__':
    main()