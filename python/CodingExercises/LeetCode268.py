'''
268. Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
'''

def LeetCode268(ary):

    ary.sort()

    fnl_lst=[]
    for i in range(1,len(ary)):

        if ary[i]-ary[i-1]>1:
            tmp=ary[i-1]+1
            while tmp<ary[i]:
                fnl_lst.append(tmp)
                tmp=tmp+1

    return fnl_lst

def main():

    ary=[3,0,1]
    print(LeetCode268(ary))

    ary = [9,6,4,2,3,5,7,0,1]
    print(LeetCode268(ary))

if __name__=='__main__':
    main()