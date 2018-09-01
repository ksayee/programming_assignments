# Find all triplets with zero sum
# Given an array of distinct elements.
# The task is to find triplets in array whose sum is zero.

def TripletSumZero(ary):

    dict={}
    fnl_lst=[]
    for i in range(0,len(ary)):
        for j in range(i+1,len(ary)):

            sum=(-1)*(ary[i]+ary[j])

            if sum in dict.keys():
                tup=tuple(sorted((sum,ary[i],ary[j])))
                if tup not in fnl_lst:
                    fnl_lst.append(tup)
            else:
                dict[ary[j]]=1

    return fnl_lst

def main():

    ary=[0, -1, 2, -3, 1]
    print(TripletSumZero(ary))

    ary = [1, -2, 1, 0, 5]
    print(TripletSumZero(ary))

if __name__=='__main__':
    main()