def twostringsum(num1,num2):

  if len(num1)>len(num2):
      maxlen=len(num1)
  else:
      maxlen=len(num2)

  carry=0
  lst=[]
  for i in range(0,maxlen):
      val=carry
      if i<len(num1):
          val=val+ord(num1[len(num1)-1-i])-48
      if i<len(num2):
          val=val+ord(num2[len(num2)-1-i])-48
      lst.append(str(val%10))
      carry=int(val/10)
  if carry>0:
      lst.append(str(carry))
  lst.reverse()
  return ''.join(lst)

def main():
    num1=str(345)
    num2=str(9874)

    print('Sum of 2 strings is:',twostringsum(num1,num2))

if __name__=='__main__':
    main()
