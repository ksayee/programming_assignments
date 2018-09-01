# Check if an array can be divided into pairs whose sum is divisible by k
# Given an array of integers and a number k,
# write a function that returns true if given array can be divided into pairs such that sum of every pair is divisible by k.

def PairsDivided(ary,k):

    fnl_lst=[]

    for i in range(0,len(ary)):
        for j in range(i+1,len(ary)):

            sum=ary[i]+ary[j]

            if sum%k==0:
                tup=(ary[i],ary[j])
                fnl_lst.append(tup)

    return fnl_lst

def main():

    ary=[9, 7, 5, 3]
    k=6
    print(PairsDivided(ary,k))

    ary = [92, 75, 65, 48, 45, 35]
    k = 10
    print(PairsDivided(ary, k))

    ary = [91, 74, 66, 48]
    k = 10
    print(PairsDivided(ary, k))

if __name__=='__main__':
    main()