# Longest subarray with sum divisible by k
# Given an arr[] containing n integers and a positive integer k.
# The problem is to find the length of the longest subarray with sum of the elements divisible by the given value k.

def LongestSubarryDivisibleK(ary,k):

    dict={}

    fnl_lst=[]

    curr_sum=0

    for i in range(0,len(ary)):
        curr_sum=curr_sum+ary[i]

        if curr_sum%k==0:
            fnl_lst.append(ary[0:i+1])
        else:

            rem=curr_sum%k

            if rem in dict.keys():
                val=dict[rem]
                for itm in val:
                    tmp=ary[itm+1:i+1]
                    if len(tmp)>0:
                        fnl_lst.append(tmp)
            else:
                tmp=[]
                tmp.append(i)
                dict[rem]=tmp

    return fnl_lst

def main():

    ary=[2, 7, 6, 1, 4, 5]
    k=3
    print(LongestSubarryDivisibleK(ary,k))

if __name__=='__main__':
    main()