# Longest Consecutive Subsequence
# Given an array of integers, find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers,
# the consecutive numbers can be in any order.

def LongestConsecutiveSubsequence(ary):

    dict={}

    for l in ary:
        if l not in dict.keys():
            dict[l]=1

    sub=[0]*len(ary)

    for i in range(0,len(ary)):

        key=ary[i]

        while key in dict.keys():
            key=key+1

        sub[i]=key-ary[i]

    return sorted(sub,reverse=True)[0]

def main():

    ary=[1, 9, 3, 10, 4, 20, 2]
    print(LongestConsecutiveSubsequence(ary))

    ary = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
    print(LongestConsecutiveSubsequence(ary))

if __name__=='__main__':
    main()