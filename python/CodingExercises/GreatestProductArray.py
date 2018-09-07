# Find pair with greatest product in array
# Given an array of n elements, the task is to find the greatest number such that it is product of two elements of given array.
# If no such element exists, print -1. Elements are within the range of 1 to 10^5.

def GreatestProductArray(ary):

    dict={}

    for l in ary:
        if l not in dict.keys():
            dict[l]=1

    fnl_lst=[]
    for i in range(0,len(ary)):
        for j in range(i+1,len(ary)):
            prd=ary[i]*ary[j]
            if prd in dict.keys():
                tup=(prd,[ary[i],ary[j]])
                fnl_lst.append(tup)

    if len(fnl_lst)==0:
        return -1
    else:
        return sorted(fnl_lst,key=lambda x:x[0],reverse=True)[0]

def main():
    
    ary=[10, 3, 5, 30, 35]
    print(GreatestProductArray(ary))

    ary = [2, 5, 7, 8]
    print(GreatestProductArray(ary))


    ary=[10, 2, 4, 30, 35]
    print(GreatestProductArray(ary))

    ary = [10, 2, 2, 4, 30, 35]
    print(GreatestProductArray(ary))

    ary = [17, 2, 1, 35, 30]
    print(GreatestProductArray(ary))

if __name__=='__main__':
    main()