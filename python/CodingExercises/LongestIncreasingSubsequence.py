# Find the length of the longest increasing subsequence in an array.

def LongestIncreasingSubsequence(ary):

    sub=[1]*len(ary)

    for i in range(1,len(ary)):
        for j in range(0,i):
            if ary[j]<ary[i]:
                tmp=sub[j]+1
                if tmp>sub[i]:
                    sub[i]=tmp

    return sorted(sub,reverse=True)[0]

def main():

    ary=[3,4,-1,0,6,2,3]
    print(LongestIncreasingSubsequence(ary))

    ary = [3, 10, 2, 1, 20]
    print(LongestIncreasingSubsequence(ary))

    ary = [3, 2]
    print(LongestIncreasingSubsequence(ary))

    ary = [50, 3, 10, 7, 40, 80]
    print(LongestIncreasingSubsequence(ary))

if __name__=='__main__':
    main()