# Find a triplet that sum to a given value
# Given an array and a value, find if there is a triplet in array whose sum is equal to the given value.
# If there is such a triplet present in array, then print the triplet and return true.
# Else return false. For example, if the given array is {12, 3, 4, 1, 6, 9} and given sum is 24,
# then there is a triplet (12, 3 and 9) present in array whose sum is 24.

def TripletSumValue(ary,k):

    fnl_lst=[]

    dict={}
    for i in range(0,len(ary)):
        for j in range(i+1,len(ary)):

            sum=ary[i]+ary[j]
            diff=k-sum

            if diff in dict.keys():
                tup=tuple(sorted((diff,ary[i],ary[j])))
                if tup not in fnl_lst:
                    fnl_lst.append(tup)
            else:
                dict[ary[j]]=1

    return fnl_lst

def main():

    ary=[12, 3, 4, 1, 6, 9]
    k=24
    print(TripletSumValue(ary,k))

    ary = [1, 4, 45, 6, 10, 8]
    k = 22
    print(TripletSumValue(ary,k))

if __name__=='__main__':
    main()