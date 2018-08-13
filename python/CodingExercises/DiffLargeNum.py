# Difference of two large numbers
# Given two numbers as strings. The numbers may be very large (may not fit in long long int), the task is to find difference of these two numbers.

def DiffLargeNum(s1,s2):

    if int(s1)>int(s2):
        big_num=list(s1)
        sml_num=list(s2)
    else:
        big_num=list(s2)
        sml_num=list(s1)

    j=len(sml_num)-1
    fnl_lst=[]
    for i in range(len(big_num)-1,-1,-1):

        if j>=0:
            if int(big_num[i])>int(sml_num[j]):
                rem=int(big_num[i])-int(sml_num[j])
            else:
                if big_num[i-1]!='0':
                    big_num[i-1]=str(int(big_num[i-1])-1)
                else:
                    big_num[i-1]=str('9')
                    big_num[i-2] = str(int(big_num[i-2]) - 1)

                rem=int(str(1)+big_num[i])-int(sml_num[j])
            j=j-1
            fnl_lst.append(str(rem))
        else:
            rem=big_num[i]
            if rem!='0':
                fnl_lst.append(str(rem))
    fnl_lst.reverse()

    return ''.join(fnl_lst)

def main():

    s1='11443333311111111100'
    s2='1144422222221111'
    print(DiffLargeNum(s1,s2))

    s1 = '122387876566565674'
    s2 = '31435454654554'
    print(DiffLargeNum(s1, s2))


if __name__=='__main__':
    main()