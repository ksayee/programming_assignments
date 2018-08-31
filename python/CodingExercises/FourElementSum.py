# Find four elements that sum to a given value | Set 3 (Hashmap)
# Given an array of integers, Check if there exist four elements at different indexes in the array whose sum is equal to a given value k.
# For example, if the given array is {1 5 1 0 6 0} and k = 7, then your function should print “YES” as (1+5+1+0=7).

def FourElementSum(ary,k):

    dict={}
    fnl_lst=[]
    for i in range(0,len(ary)):
        for j in range(i+1,len(ary)):

            sum=ary[i]+ary[j]

            diff=k-sum

            if diff in dict.keys():
                val=dict[diff]
                tmp=[val[0],val[1],i,j]
                if len(set(tmp))==4:
                    tup=(i,j,val[0],val[1])
                    fnl_lst.append(tup)
            else:
                tup=(i,j)
                dict[sum]=tup

    return fnl_lst

def main():

    ary=[1,5,1,0,6,0]
    k=7
    print(FourElementSum(ary,k))

    ary = [38,7,44,42,28,16,10,37,33,2,38,29,26,8,25]
    k = 22
    print(FourElementSum(ary, k))

if __name__=='__main__':
    main()