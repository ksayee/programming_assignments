# Find distinct elements common to all rows of a matrix
# Given a n x n matrix. The problem is to find all the distinct elements common to all rows of the matrix.
# The elements can be printed in any order.

def CommonElementsRowsMatrix(mat):

    dict={}
    lgt=len(mat)
    for itm in mat:
        lst=set(itm)
        for l in lst:
            if l in dict.keys():
                dict[l]=dict.get(l)+1
            else:
                dict[l]=1

    fnl_lst=[]

    for key,val in dict.items():
        if val==lgt:
            fnl_lst.append(key)
    return fnl_lst

def main():
    
    mat=[[2, 1, 4, 3],[1, 2, 3, 2],[3, 6, 2, 3],[5, 2, 5, 3]]
    print(CommonElementsRowsMatrix(mat))

    mat = [[12, 1, 14, 3, 16], [14, 2, 1, 3, 35], [14, 1, 14, 3, 11], [14, 25, 3, 2, 1], [1, 18, 3, 21, 14]]
    print(CommonElementsRowsMatrix(mat))

if __name__=='__main__':
    main()