def Add2List(ary1,ary2):

    big_lst=[]
    sml_lst=[]

    if len(ary1)>len(ary2):
        big_lst=ary1
        sml_lst=ary2
    else:
        big_lst=ary2
        sml_lst=ary1

    carry=0
    j=len(sml_lst)-1
    fnl_lst=[]

    for i in range(len(big_lst)-1,-1,-1):
        if j>=0:
            val=big_lst[i]+sml_lst[j]+carry
            fnl_lst.append(str(val%10))
            carry=int(val/10)
            j=j-1
        else:
            val = big_lst[i] + carry
            fnl_lst.append(str(val % 10))
            carry = int(val / 10)

    if carry>0:
        fnl_lst.append(str(carry))
    fnl_lst.reverse()
    print(int(''.join(fnl_lst)))
    
def main():

    ary1=[9,9,9,7]
    ary2=[4,8,9]
    Add2List(ary1,ary2)

if __name__=='__main__':
    main()