# Largest Sum Contiguous Subarray
# Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum.

def LargestSumContigousSubArray(ary):

    lst=[0]*len(ary)

    sum=0
    for i in range(0,len(ary)):
        sum=sum+ary[i]
        lst[i]=sum

    max=0
    idx=0
    for i in range(1,len(lst)):
        if lst[i]>max:
            max=lst[i]
            idx=i

    for i in range(1,i):
        if lst[i]<lst[i-1]:
            continue
        else:
            break

    return ary[i:idx+1]

def main():

    ary=[-2, -3, 4, -1, -2, 1, 5, -3]
    print(LargestSumContigousSubArray(ary))

    ary = [1, -2, 1, 1, -2, 1]
    print(LargestSumContigousSubArray(ary))

if __name__=='__main__':
    main()