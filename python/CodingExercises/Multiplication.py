def convert_to_list(s):
    return list(s)

def Multiplication(s1,s2):

    lst1=convert_to_list(s1)
    lst2=convert_to_list(s2)
    print("List 1:",lst1)
    print("List 2:",lst2)

    carry_a=0
    carry_p=0
    fnl_lst=[]

    for i in range(len(lst2)-1,-1,-1):
        k=(len(lst2)-1)-i
        tmp2=int(lst2[i])
        for j in range(len(lst1)-1,-1,-1):
            tmp1=int(lst1[j])
            if k==0:
                num=carry_a+(tmp1*tmp2)
                rem=num%10
                carry_a=int(num/10)
                fnl_lst.append(str(rem))
            elif k!=0:
                num1=carry_a+(tmp1*tmp2)
                num=carry_p + int(fnl_lst[k])+num1%10
                rem=num%10
                carry_p=int(num/10)
                fnl_lst[k]=str(rem)
                carry_a=int(num1/10)

                if k<len(fnl_lst)-1:
                    k=k+1
        if k!=0:
            if k<=(len(fnl_lst)-1) and (carry_a+carry_p)!=0:
                fnl_lst.append(str(carry_p+carry_a))
        else:
            if carry_a!=0:
                fnl_lst.append(carry_a)
            carry_a=0

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


if __name__=='__main__':
    main()