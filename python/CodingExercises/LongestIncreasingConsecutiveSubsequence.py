# Longest Increasing consecutive subsequence
# Given N elements, write a program that prints the length of the longest increasing subsequence whose adjacent element difference is one.

def LongestIncreasingConsecutiveSubsequence(ary):

    sub=[1]*len(ary)

    for i in range(1,len(ary)):
        for j in range(0,i):
            if ary[i]-ary[j]==1:
                tmp=sub[j]+1
                if tmp>sub[i]:
                    sub[i]=tmp

    return sorted(sub,reverse=True)[0]

def main():

    ary=[3, 10, 3, 11, 4, 5, 6, 7, 8, 12]
    print(LongestIncreasingConsecutiveSubsequence(ary))

    ary = [6, 7, 8, 3, 4, 5, 9, 10]
    print(LongestIncreasingConsecutiveSubsequence(ary))

if __name__=='__main__':
    main()