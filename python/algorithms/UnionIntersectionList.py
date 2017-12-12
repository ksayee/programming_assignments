def unionintersect(lst1,lst2):

  dict={}

  for i in range(0,len(lst1)):
      key=lst1[i]
      if key in dict.keys():
          dict[key]=1
      else:
          dict[key]=1

  un_lst=[]
  for i in range(0,len(lst2)):
      key=lst2[i]
      if key in dict.keys():
          un_lst.append(key)
      else:
          dict[key]=1

  int_lst=[]
  for key,val in dict.items():
      int_lst.append(key)
  print('Union of List is:',un_lst)
  print('Intersection of List is:',int_lst)


def main():
    lst1=[1,3,4,5,7]
    lst2=[2,3,5,6]

    unionintersect(lst1,lst2)

if __name__=='__main__':
    main()
