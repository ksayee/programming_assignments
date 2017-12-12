
def emp_mag(lst):



   fnl_lst={}

   for key, val in lst.items():
       emp=key
       mgr=val
       if emp==mgr:
           continue
       if mgr in fnl_lst.keys():
           fnl_lst[mgr].append(emp)
       else:
           fnl_lst[mgr]=[]
           fnl_lst[mgr].append(emp)

   for key, val in fnl_lst.items():
       print(key,val)

def main():

    lst={}
    lst['A']='C'
    lst['B'] = 'C'
    lst['C'] = 'F'
    lst['D'] = 'E'
    lst['E'] = 'F'
    lst['F'] = 'F'

    emp_mag(lst)
if __name__=='__main__':
    main()
