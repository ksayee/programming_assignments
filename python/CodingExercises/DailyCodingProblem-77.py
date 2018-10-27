'''
This problem was asked by Snapchat.
Given a list of possibly overlapping intervals, return a new list of intervals where all
overlapping intervals have been merged.
The input list is not necessarily ordered in any way.
For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20,
25)].
'''

def DailyCodingProblem77(ary):

    sort_lst=sorted(ary,key=lambda x:x[0])

    fnl_lst=[]
    fnl_lst.append(sort_lst[0])
    k=0

    for i in range(1,len(sort_lst)):

        tmp=sort_lst[i]

        if tmp[0]>fnl_lst[k][0] and tmp[0]<fnl_lst[k][1]:
            if tmp[1]<fnl_lst[k][1]:
                continue
            else:
                tup=(fnl_lst[k][0],tmp[1])
                del fnl_lst[k]
                fnl_lst.append(tup)
        else:
            fnl_lst.append(tmp)
            k=k+1

    return fnl_lst

def main():

    ary=[(1, 3), (5, 8), (4, 10), (20, 25)]
    print(DailyCodingProblem77(ary))

if __name__=='__main__':
    main()