# Size of The Subarray With Maximum Sum
# An array is given, find length of the subarray having maximum sum.

def SubArraryMaxSum(ary):

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

    for i in range(1,len(lst)):
        if lst[i]<lst[i-1]:
            continue
        else:
            break

    return ary[i:idx+1]

def main():

    ary=[1, -2, 1, 1, -2, 1]
    print(SubArraryMaxSum(ary))

    ary = [-2, -3, 4, -1, -2, 1, 5, -3 ]
    print(SubArraryMaxSum(ary))

    ary = [-2,7,-6,-1,5,6,-3]
    print(SubArraryMaxSum(ary))

if __name__=='__main__':
    main()