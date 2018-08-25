# Equilibrium index of an array
# Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
# For example, in an array A:
# Input : A[] = {-7, 1, 5, 2, -4, 3, 6}
# Output : 3
# 3 is an equilibrium index, because:
# A[0] + A[1] + A[2]  =  A[4] + A[5] + A[6]

def EqulibriumIndex(ary):

    sum=0
    left_sum=0

    for i in range(0,len(ary)):
        sum=sum+ary[i]

    for i in range(0,len(ary)):

        sum=sum-ary[i]
        if left_sum==sum and i!=len(ary)-1:
            return i
        else:
            left_sum=left_sum+ary[i]

    return -1

def main():
    
    ary=[-7, 1, 5, 2, -4, 3, 6]
    print(EqulibriumIndex(ary))

    ary = [-7, 1, 5, 2, -4, 3, 0]
    print(EqulibriumIndex(ary))

if __name__=='__main__':
    main()