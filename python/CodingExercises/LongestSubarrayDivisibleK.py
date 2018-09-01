# Longest subarray with sum divisible by k
# Given an arr[] containing n integers and a positive integer k.
# The problem is to find the length of the longest subarray with sum of the elements divisible by the given value k.

def LongestSubarryDivisibleK(ary,k):

    fnl_lst=[]

    dict={}
    sum=0
    for i in range(0,len(ary)):
        sum=sum+ary[i]

        if sum%k==0:
            tup=(0,i)
            fnl_lst.append(tup)
        else:
            rem=sum%k

            if rem in dict.keys():
                val=dict[rem]
                for idx in val:
                    tup=(idx+1,i)
                    fnl_lst.append(tup)
                dict[rem].append(i)
            else:
                tmp=[]
                tmp.append(i)
                dict[rem]=tmp

    max=0
    for l in fnl_lst:
        if l[1]-l[0]>max:
            max=l[1]-l[0]
            tup=l

    return ary[tup[0]:tup[1]+1]

def main():

    ary=[2, 7, 6, 1, 4, 5]
    k=3
    print(LongestSubarryDivisibleK(ary,k))

if __name__=='__main__':
    main()