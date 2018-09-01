# Find four elements a, b, c and d in an array such that a+b = c+d
# Given an array of distinct integers,
# find if there are two pairs (a, b) and (c, d) such that a+b = c+d, and a, b, c and d are distinct elements.
# If there are multiple answers, then print any of them.

def PairFourElementSum(ary):

    dict={}

    fnl_lst=[]
    for i in range(0,len(ary)):
        for j in range(i+1,len(ary)):

            sum=ary[i]+ary[j]

            if sum in dict.keys():
                val=dict[sum]
                tup=(val[0],val[1],ary[i],ary[j])
                if len(set(tup))==4:
                    fnl_lst.append(tup)
            else:
                tup=(ary[i],ary[j])
                dict[sum]=tup

    return fnl_lst

def main():

    ary=[3, 4, 7, 1, 2, 9, 8]
    print(PairFourElementSum(ary))

    ary = [3, 4, 7, 1, 12, 9]
    print(PairFourElementSum(ary))

    ary = [65, 30, 7, 90, 1, 9, 8]
    print(PairFourElementSum(ary))

if __name__=='__main__':
    main()