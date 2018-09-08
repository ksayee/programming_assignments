# Find the largest subarray with 0 sum
# Given an array of integers, find length of the largest subarray with sum equals to 0.

def LargestSubArraySumZero(ary,k):

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
    
    ary=[15, -2, 2, -8, 1, 7, 10, 23]
    k=0
    print(LargestSubArraySumZero(ary,k))

    ary = [1, 2, 3]
    k = 0
    print(LargestSubArraySumZero(ary,k))

    ary = [1, 0, 3]
    k = 0
    print(LargestSubArraySumZero(ary,k))

if __name__=='__main__':
    main()