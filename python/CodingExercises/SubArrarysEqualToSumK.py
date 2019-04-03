'''
Number of subarrays having sum exactly equal to k
Given an unsorted array of integers, find the number of subarrays having sum exactly equal to a given number k.

Examples:

Input : arr[] = {10, 2, -2, -20, 10},
        k = -10
Output : 3
Subarrays: arr[0...3], arr[1...4], arr[3..4]
have sum exactly equal to -10.

Input : arr[] = {9, 4, 20, 3, 10, 5},
            k = 33
Output : 2
Subarrays : arr[0...2], arr[2...4] have sum
exactly equal to 33.
'''

def SubArrarysEqualToSumK(ary,k):

    dict={}

    curr_sum=0
    fnl_lst=[]

    for i in range(0,len(ary)):

        curr_sum=curr_sum+ary[i]

        if curr_sum==k:
            fnl_lst.append(ary[:i+1])

        if curr_sum not in dict.keys():
            tmp=[]
            tmp.append(i)
            dict[curr_sum]=tmp
        else:
            dict[curr_sum].append(i)

        diff=curr_sum-k

        if diff in dict.keys():
            val=dict[diff]
            for l in val:
                fnl_lst.append(ary[l+1:i+1])

    return fnl_lst

def main():
    
    ary=[10, 2, -2, -20, 10]
    k=-10
    print(SubArrarysEqualToSumK(ary,k))

    ary = [9, 4, 20, 3, 10, 5]
    k = 33
    print(SubArrarysEqualToSumK(ary, k))

if __name__=='__main__':
    main()