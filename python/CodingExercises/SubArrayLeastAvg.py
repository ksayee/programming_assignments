# Find the subarray with least average
# Given an array arr[] of size n and integer k such that k <= n.

def SubArrayLeastAvg(ary,n):

    min_sum=999
    curr_sum=0
    for i in range(0,len(ary)):
        if i<n:
            curr_sum=curr_sum+ary[i]
        else:
            break
    min_sum = curr_sum
    min_idx=(0,n-1)
    j=n
    for k in range(j,len(ary)):
        curr_sum=curr_sum+ary[k]-ary[k-n]
        if curr_sum<min_sum:
            min_sum=curr_sum
            min_idx=(k-n,k)

    lst=ary[min_idx[0]:min_idx[1]]
    return lst

def main():

    ary=[3, 7, 90, 20, 10, 50, 40]
    n=3
    print(SubArrayLeastAvg(ary,n))

    ary = [3, 7, 5, 20, -10, 0, 12]
    n = 2
    print(SubArrayLeastAvg(ary,n))

if __name__=='__main__':
    main()