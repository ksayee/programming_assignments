# Find maximum average subarray of k length
# Given an array with positive and negative numbers, find the maximum average subarray of given length.

def MaximumAverage(ary,k):

    curr_sum=0


    for i in range(0,len(ary)):
        if i<k:
            curr_sum=curr_sum+ary[i]
        else:
            break
    max_idx=(0,k-1)
    max_sum = curr_sum
    j=k
    for i in range(j,len(ary)):

        curr_sum=curr_sum+ary[i]-ary[i-k]
        if curr_sum>max_sum:
            max_sum=curr_sum
            max_idx=((i-k+1),i)

    return ary[max_idx[0]:max_idx[1]+1]

def main():
    
    ary=[1, 12, -5, -6, 50, 3]
    k=4
    print(MaximumAverage(ary,k))

if __name__=='__main__':
    main()