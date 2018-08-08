# Python | Remove leading zeros from an IP address
# Given an IP address, remove leading zeros from the IP address.

def RemoveLeadingZeros(s1):

    lst=s1.split('.')

    fnl_lst=[]
    tmp_lst=[]
    for l in lst:

        tmp=list(l)
        tmp_lst=[]
        flg=True
        for k in tmp:

            if flg==True and k=='0':
                continue
            else:
                tmp_lst.append(k)
                flg=False
        fnl_lst.append(''.join(tmp_lst))

    return '.'.join(fnl_lst)

def main():

    s1='100.020.003.400'
    print(RemoveLeadingZeros(s1))

    s1 = '001.200.001.004'
    print(RemoveLeadingZeros(s1))


if __name__=='__main__':
    main()