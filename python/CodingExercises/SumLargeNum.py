# Sum of two large numbers
# Given two numbers as strings. The numbers may be very large (may not fit in long long int), the task is to find sum of these two numbers.

def SumLargeNum(s1,s2):

    if len(s1)>len(s2):
        big_num=s1
        sml_num=s2
    else:
        big_num=s2
        sml_num=s1

    carry=0
    j=len(sml_num)-1
    fnl_lst=[]
    for i in range(len(big_num)-1,-1,-1):

        if j>=0:
            tmp_sum=int(big_num[i])+int(sml_num[j])+carry
            j=j-1
        else:
            tmp_sum = int(big_num[i]) + carry
        rem=tmp_sum%10
        carry=int(tmp_sum/10)
        fnl_lst.append(str(rem))

    if carry>0:
        fnl_lst.append(carry)
    fnl_lst.reverse()

    return ''.join(fnl_lst)

def main():

    s1='3333311111111111'
    s2='44422222221111'
    print(SumLargeNum(s1,s2))

    s1 = '7777555511111111'
    s2 = '3332222221111'
    print(SumLargeNum(s1, s2))


if __name__=='__main__':
    main()