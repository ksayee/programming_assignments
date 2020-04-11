'''
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

'''

def LeetCode498(matrix):

    output_lst=[]
    flg=False
    for k in range(0,len(matrix)):
        tmp=[]
        i=k
        j=0
        while i>=0:
            tmp.append(matrix[i][j])
            i=i-1
            j=j+1
        if flg==True:
            tmp.reverse()
            output_lst.extend(tmp)
            flg=False
        elif flg==False:
            output_lst.extend(tmp)
            flg=True

    flg=True
    for k in range(1,len(matrix[0])):
        tmp=[]
        i=len(matrix)-1
        j=k
        while j<len(matrix[0]):
            tmp.append(matrix[i][j])
            i=i-1
            j=j+1
        if flg==True:
            tmp.reverse()
            output_lst.extend(tmp)
            flg=False
        elif flg==False:
            output_lst.extend(tmp)
            flg=True
    return output_lst

def main():

    matrix=[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
    print(LeetCode498(matrix))


if __name__=='__main__':
    main()