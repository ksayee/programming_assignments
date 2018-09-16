'''
18. 4Sum

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

def LeetCode18(ary):

    tmp_lst=[]
    fnl_lst=[]
    k=0
    dict={}
    for i in range(0,len(ary)):
        for j in range(i+1,len(ary)):

            sum=ary[i]+ary[j]
            diff=k-sum
            if diff in dict.keys():
                for tup in dict[diff]:
                    tmp=[]
                    for l in tup:
                        tmp.append(l)
                    tmp.append(i)
                    tmp.append(j)

                if len(set(tmp))==4:
                    tup=tuple(sorted(tmp))
                    if tup not in tmp_lst:
                        tmp_lst.append(tup)

            if sum in dict.keys():
                tup=(i,j)
                dict[sum].append(tup)
            else:
                tmp=[]
                tup=(i,j)
                tmp.append(tup)
                dict[sum]=tmp

    for l in tmp_lst:
        tmp=[]
        for idx in l:
            tmp.append(ary[idx])
        fnl_lst.append(tmp)

    return fnl_lst

def main():
    
    ary=[1, 0, -1, 0, -2, 2]
    print(LeetCode18(ary))

if __name__=='__main__':
    main()