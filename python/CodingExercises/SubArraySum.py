# Find if there is a subarray with 0 sum
# Given an array of positive and negative numbers,
# find if there is a subarray (of size at-least one) with 0 sum.

def SubArrarySum(ary):

    dict={}

    sum=0
    fnl_lst=[]
    for i in range(0,len(ary)):

        sum=sum+ary[i]

        if ary[i]==0:
            tup=(i,i)
            fnl_lst.append(tup)
            break
        elif sum==0 and sum not in dict.keys():
            tup(i-1,i)
            fnl_lst.append(tup)
            break
        elif sum in dict.keys():
            tup=(dict[sum]+1,i)
            fnl_lst.append(tup)
            break

        dict[sum]=i

    return fnl_lst

def main():
    
    ary=[4, 2, -3, 1, 6]
    print(SubArrarySum(ary))

    ary = [4, 2, 0, 1, 6]
    print(SubArrarySum(ary))

    ary = [1, 4, -2, -2, 5, -4, 3]
    print(SubArrarySum(ary))

    ary = [-3, 2, 3, 1, 6]
    print(SubArrarySum(ary))

if __name__=='__main__':
    main()