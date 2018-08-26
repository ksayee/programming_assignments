# Print all subarrays with 0 sum
# Given an array, print all subarrays in the array which has sum 0.

def AllSubArraySum(ary):

    dict={}
    sum=0
    fnl_lst=[]
    for i in range(0,len(ary)):

        sum=sum+ary[i]

        if sum==0:
            tup=(0,i)
            fnl_lst.append(tup)
        else:
            if sum in dict.keys():
                val=dict[sum]
                for idx in val:
                    tup=(idx+1,i)
                    fnl_lst.append(tup)
                dict[sum].append(i)
            else:
                tmp=[]
                tmp.append(i)
                dict[sum]=tmp
    return fnl_lst

def main():
    
    ary=[6, 3, -1, -3, 4, -2, 2,4, 6, -12, -7]
    print(AllSubArraySum(ary))

if __name__=='__main__':
    main()