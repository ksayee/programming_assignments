#Program to add a single number to that number in list
#eg: 9997+9=10006
def plusone(lst,num):

  carry=num
  fnl=[]
  for i in range(len(lst)-1,-1,-1):
      val=lst[i]+carry
      fnl.append(str(val%10))
      carry=int(val/10)

  if carry>0:
      fnl.append(str(carry))

  fnl.reverse()
  print(''.join(fnl))

def plusone_num(act_num,num):

    carry=num

    fnl_lst=[]
    while act_num!=0:
        val=(act_num%10)+carry
        fnl_lst.append(str(val%10))
        carry=int(val/10)
        act_num=int(act_num/10)

    if carry>0:
        fnl_lst.append(str(carry))

    fnl_lst.reverse()
    print(''.join(fnl_lst))

def main():
    lst=[9,9,9,7]
    num=9
    plusone(lst,num)

    act_num=9997
    num=9
    plusone_num(act_num,num)

if __name__=='__main__':
    main()
