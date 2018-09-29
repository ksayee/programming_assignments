'''
886. Possible Bipartition
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
Each person may dislike some other people, and they should not go into the same group.
Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
Return true if and only if it is possible to split everyone into two groups in this way.
'''

def LeetCode886(n,dislikes):

    i=1
    lst=[]
    while i<=n:
        lst.append(i)
        i=i+1

    tmp=[]
    fnl_lst=[]

    Combinations_recur(lst,tmp,fnl_lst)

    res_lst=[]

    for l in fnl_lst:
        if l in dislikes:
            continue
        else:
            res_lst.append(l)
    if len(res_lst)>0:
        return True
    else:
        return False

def Combinations_recur(lst,tmp,fnl_lst):

    if len(tmp)==2:
        if sorted(tmp) not in fnl_lst:
            fnl_lst.append(sorted(tmp.copy()))
        return

    for i in range(0,len(lst)):
        tmp.append(lst[i])
        Combinations_recur(lst[i+1:],tmp, fnl_lst)
        tmp.pop()

def main():

    n=4
    dislikes=[[1,2],[1,3],[2,4]]
    print(LeetCode886(n,dislikes))

    n = 3
    dislikes = [[1,2],[1,3],[2,3]]
    print(LeetCode886(n, dislikes))

    n = 5
    dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
    print(LeetCode886(n, dislikes))

if __name__=='__main__':
    main()