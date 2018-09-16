'''
15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

def LeetCode15(ary):

    fnl_lst=[]
    k=0

    for i in range(0,len(ary)):
        dict={}
        for j in range(i+1,len(ary)):

            sum=ary[i]+ary[j]

            diff=k-sum

            if diff in dict.keys():
                tup=tuple(sorted((ary[i],ary[j],diff)))
                if tup not in fnl_lst:
                    fnl_lst.append(tup)
            else:
                dict[ary[j]]=1

    return fnl_lst

def main():
    
    ary=[-1, 0, 1, 2, -1, -4]
    print(LeetCode15(ary))

if __name__=='__main__':
    main()