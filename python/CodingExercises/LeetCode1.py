'''
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


def LeetCode1(ary,k):

    dict={}
    fnl_lst=[]
    for i in range(0,len(ary)):

        key=ary[i]
        diff=k-key

        if diff in dict.keys():
            val=dict[diff]
            tup=(i,val)
            fnl_lst.append(tup)
        else:
            dict[key]=i
    return fnl_lst

def main():

    ary=[2, 7, 11, 15]
    k=9
    print(LeetCode1(ary,k))

if __name__=='__main__':
    main()