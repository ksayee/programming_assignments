'''
415. Add Strings
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
Note:
The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

def LeetCode415(num1,num2):

    if len(num1)>len(num2):
        big_lst=list(num1)
        sml_lst=list(num2)
    else:
        big_lst=list(num2)
        sml_lst=list(num1)

    fnl_lst=[]
    j=len(sml_lst)-1
    carry=0
    for i in range(len(big_lst)-1,-1,-1):

        if j>=0:
            val=int(big_lst[i])+int(sml_lst[j])+carry
            j=j-1
        else:
            val = int(big_lst[i]) + carry
        fnl_lst.append(str(val%10))
        carry=val//10

    if carry>0:
        fnl_lst.append(str(carry))

    fnl_lst.reverse()
    return ''.join(fnl_lst)

def main():

    num1='345'
    num2='9845'
    print(LeetCode415(num1,num2))

if __name__=='__main__':
    main()