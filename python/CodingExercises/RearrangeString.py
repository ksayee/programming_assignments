# Rearrange a string in sorted order followed by the integer sum
# Given a string containing uppercase alphabets and integer digits (from 0 to 9),
# the task is to print the alphabets in the order followed by the sum of digits.

def RearrangeString(str1):

    lst=list(str1)

    sum=0
    tmp=[]
    for l in lst:
        if l>='0' and l<='9':
            sum=sum+int(l)
        else:
            tmp.append(l)

    sort=sorted(tmp)

    return ''.join(sort)+str(sum)

def main():
    
    str1='AC2BEW3'
    print(RearrangeString(str1))

    str1 = 'ACCBA10D2EW30'
    print(RearrangeString(str1))

if __name__=='__main__':
    main()