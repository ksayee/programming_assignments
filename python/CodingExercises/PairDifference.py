# Find a pair with the given difference
# Given an unsorted array and a number n,
# find if there exists a pair of elements in the array whose difference is n.

def PairDifference(ary,k):

    dict={}
    fnl_lst=[]
    for i in range(0,len(ary)):

        diff=abs(k-ary[i])
        if diff in dict.keys():
            tup=(ary[i],diff)
            fnl_lst.append(tup)
        else:
            dict[ary[i]]=1

    return fnl_lst

def main():

    ary=[5, 20, 3, 2, 50, 80]
    k=78
    print(PairDifference(ary,k))

    ary = [90, 70, 20, 80, 50]
    k = 45
    print(PairDifference(ary, k))

if __name__=='__main__':
    main()