def convert_to_list(s):
    return list(s)

def Multiplication(s1,s2):

    lst1=convert_to_list(s1)
    lst2=convert_to_list(s2)
    print("List 1:",lst1)
    print("List 2:",lst2)

    carry_a=0
    carry_p=0
    flg=True
    fnl_lst=[]

    for i in range(len(lst2)-1,-1,-1):
        tmp2=int(lst2[i])
        k=(len(lst2)-1)-i
        for j in range(len(lst1)-1,-1,-1):
            tmp1=int(lst1[j])

            if k==0:
                num=carry_a+(tmp2*tmp1)
                rem=num%10
                fnl_lst.append(str(rem))
                carry_a=int(num/10)
            else:
                num1=carry_a+(tmp1*tmp2)

                if flg==True:
                    num=carry_p+int(fnl_lst[k])+(num1%10)
                else:
                    num=carry_p+(num1%10)

                rem=num%10
                carry_a = int(num1 / 10)
                carry_p=int(num/10)
                if k<=len(fnl_lst)-1 and flg==True:
                    fnl_lst[k]=str(rem)

                if flg == False:
                    fnl_lst.append(str(rem))
                    k=k+1
                    carry_p=0

                if k<len(fnl_lst)-1:
                    k=k+1
                else:
                    flg=False

        if k==0:
            if carry_a!=0:
                fnl_lst.append(str(carry_a))
        else:
            if carry_a+carry_p!=0:
                fnl_lst.append(str(carry_p+carry_a))
        flg=True
        carry_a=0
        carry_p=0

    fnl_lst.reverse()
    return ''.join(fnl_lst)

def main():

    s1='25'
    s2='76'
    print(Multiplication(s1,s2))

    s1 = '345'
    s2 = '89'
    print(Multiplication(s1, s2))

    s1='978'
    s2='89'
    print(Multiplication(s1,s2))

    s1 = '123'
    s2 = '456'
    print(Multiplication(s1, s2))

    s1 = '99'
    s2 = '88888'
    print(Multiplication(s1, s2))

if __name__=='__main__':
    main()