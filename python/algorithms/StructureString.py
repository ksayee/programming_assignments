def StructureString(str1):

  fnl_str=''
  found=False
  spc_flg=False
  print(str1,len(str1))
  for i in range(0,len(str1)):
      if str1[i]==' ' and found==False:
          continue
      elif str1[i]!=' ' and spc_flg==True:
          fnl_str=fnl_str+' '+str1[i]
          spc_flg=False
      elif str1[i]!=' ':
          fnl_str=fnl_str+str1[i]
          found=True
      elif str1[i]==' ':
          spc_flg=True
      else:
          continue

      prev_char=str1[i]

  print(fnl_str,len(fnl_str))

def main():
    str1 = '    The     sky is     very blue     '
    StructureString(str1)

if __name__=='__main__':
    main()