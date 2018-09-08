# Find subarray with given sum | Set 2 (Handles Negative Numbers)
# Given an unsorted array of integers, find a subarray which adds to a given number.
# If there are more than one subarrays with sum as the given number, print any of them.

def SubArrayGivenSum(ary,k):

    dict={}
    curr_sum=0
    fnl_lst=[]

    for i in range(0,len(ary)):

        curr_sum=curr_sum+ary[i]

        if curr_sum==k:
            fnl_lst.append(ary[0:i+1])
        else:
            if curr_sum in dict.keys():
                dict[curr_sum].append(i)
            else:
                tmp=[]
                tmp.append(i)
                dict[curr_sum]=tmp

            diff=curr_sum-k

            if diff in dict.keys():
                val=dict[diff]
                for itm in val:
                    tmp=ary[itm+1:i+1]
                    if len(tmp)>0:
                        fnl_lst.append(ary[itm+1:i+1])

    return fnl_lst

def main():

    ary=[9, 4, 20, 3, 10, 5]
    k=33
    print(SubArrayGivenSum(ary,k))

    ary = [10, 2, -2, -20, 10]
    k = -10
    print(SubArrayGivenSum(ary, k))

    ary = [-10, 0, 2, -2, -20, 10]
    k = 20
    print(SubArrayGivenSum(ary, k))

if __name__=='__main__':
    main()