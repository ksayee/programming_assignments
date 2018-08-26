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

def EmployeeManager(ary):

    dict={}

    lst=[]
    for l in ary:

        emp=l[0]
        mgr=l[1]

        lst.append(emp)
        lst.append(mgr)
        if emp!=mgr:
            if mgr in dict.keys():
                dict[mgr].append(emp)
            else:
                tmp=[]
                tmp.append(emp)
                dict[mgr]=tmp

    dst_lst=set(lst)

    fnl_lst=[]
    for l in dst_lst:
        cnt=0
        if l in dict.keys():
            cnt=cnt+len(dict[l])
            val=dict[l]
            for k in val:
                if k in dict.keys():
                    cnt=cnt+len(dict[k])
        tup=(l,cnt)
        fnl_lst.append(tup)

    return fnl_lst

def main():
    
    ary=[('A','C'),('B','C'),('C','F'),('D','E'),('E','F'),('F','F')]
    print(EmployeeManager(ary))

if __name__=='__main__':
    main()