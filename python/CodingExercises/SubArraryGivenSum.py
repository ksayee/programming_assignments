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
            tup=(0,i)
            fnl_lst.append(ary[tup[0]:tup[1]+1])
        else:
            diff=curr_sum-k

            if diff in dict.keys():
                val=dict[diff]
                for idx in val:
                    tup=(idx+1,i)
                    fnl_lst.append(ary[tup[0]:tup[1]+1])
                dict[diff].append(i)
            else:
                tmp=[]
                tmp.append(i)
                dict[curr_sum]=tmp
    return fnl_lst

def main():

    ary=[1, 4, 20, 3, 10, 5]
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