
def singlenumber(ary):

   lst={}

   for i in range(0,len(ary)):
       key=ary[i]

       if key in lst.keys():
           lst[key]=lst.get(key)+1
       else:
           lst[key]=1

   for key,val in lst.items():
       if val==1:
           print(key)

def main():
    ary = [2, 4, 2, 3, 5, 4, 7,8,5,3, 8, 7, 9, 0, 0]
    singlenumber(ary)

if __name__=='__main__':
    main()
