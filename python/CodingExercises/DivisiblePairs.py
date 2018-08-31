# Count divisible pairs in an array
# Given an array, count pairs in the array such that one element of pair divides other.

def DivisiblePairs(ary):

    fnl_lst=[]

    for i in range(0,len(ary)):
        for j in range(i+1,len(ary)):

            if (ary[i]%ary[j]==0 or ary[j]%ary[i]==0):
                tup=(ary[i],ary[j])
                fnl_lst.append(tup)

    return fnl_lst

def main():

    ary=[1, 2, 3]
    print(DivisiblePairs(ary))

    ary = [2, 3, 5, 7]
    print(DivisiblePairs(ary))

if __name__=='__main__':
    main()