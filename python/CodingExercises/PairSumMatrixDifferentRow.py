# Find pairs with given sum such that elements of pair are in different rows
# Given a matrix of distinct values and a sum.
# The task is to find all the pairs in given whose summation is equal to given sum.
# Each element of pair must be from different rows i.e; pair must not lie in same row.

def PairSumMatrixDifferentRow(mat,n):

    dict={}

    fnl_lst=[]
    for i in range(0,len(mat)):

        itm=mat[i]

        for num in itm:
            sum=n-num
            if sum in dict.keys():
                val=dict[sum]
                if val!=i:
                    tup=(num,sum)
                    fnl_lst.append(tup)
            else:
                dict[num]=i

    return fnl_lst

def main():
    
    mat=[[1, 3, 2, 4],[5, 8, 7, 6],[9, 10, 13, 11],[12, 0, 14, 15]]
    n=11
    print(PairSumMatrixDifferentRow(mat,n))

if __name__=='__main__':
    main()