# Longest subsequence such that difference between adjacents is one | Set 2
# Given an array of size n. The task is to find the longest subsequence such that difference between adjacents is one.
# Time Complexity of O(n) is required.

def LongestSubsequenceAdjDiffOne(ary):

    sub=[1]*len(ary)

    for i in range(1,len(ary)):
        for j in range(0,i):

            if abs(ary[i]-ary[j])==1:
                tmp=sub[j]+1

                if tmp>sub[i]:
                    sub[i]=tmp

    return sorted(sub,reverse=True)[0]

def main():

    ary=[10, 9, 4, 5, 4, 8, 6]
    print(LongestSubsequenceAdjDiffOne(ary))

    ary = [1, 2, 3, 2, 3, 7, 2, 1]
    print(LongestSubsequenceAdjDiffOne(ary))

if __name__=='__main__':
    main()