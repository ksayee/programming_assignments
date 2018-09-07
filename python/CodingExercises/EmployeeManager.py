# Find number of Employees Under every Employee
# Given a dictionary that contains mapping of employee and his manager as a number of (employee, manager) pairs like below.
# { "A", "C" },
# { "B", "C" },
# { "C", "F" },
# { "D", "E" },
# { "E", "F" },
# { "F", "F" }
# In this example C is manager of A,
# C is also manager of B, F is manager
# of C and so on.

def find_employee(lst,cnt,dict):

    if len(lst)==0:
        return 0

    for l in lst:
        if l in dict.keys():
            cnt=len(dict[l])+find_employee(dict[l],cnt,dict)

    return cnt

def EmployeeManager(ary):

    dict={}

    lst=[]
    for key in ary:
        emp=key[0]
        mgr=key[1]

        lst.append(emp)
        lst.append(mgr)
        if emp!=mgr:
            if mgr in dict.keys():
                dict[mgr].append(emp)
            else:
                tmp=[]
                tmp.append(emp)
                dict[mgr]=tmp

    lst_set=set(lst)

    fnl_lst=[]
    for itm in lst_set:

        cnt=0
        if itm in dict.keys():
            cnt=len(dict[itm])+find_employee(dict[itm],cnt,dict)
        tup=(itm,cnt)
        fnl_lst.append(tup)

    return sorted(fnl_lst,key=lambda x:x[0])

def main():
    
    ary=[('A','C'),('B','C'),('C','F'),('D','E'),('E','F'),('F','F'),('G','A')]
    print(EmployeeManager(ary))

if __name__=='__main__':
    main()