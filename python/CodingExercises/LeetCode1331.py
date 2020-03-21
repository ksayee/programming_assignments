'''
1331. Rank Transform of an Array
Given an array of integers arr, replace each element with its rank.
The rank represents how large the element is. The rank has the following rules:
Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
Example 1:
Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
Example 2:
Input: arr = [100,100,100]
Output: [1,1,1]
Explanation: Same elements share the same rank.
Example 3:
Input: arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]
'''

def LeetCode1331(ary):

    sort_lst=sorted(set(ary))
    rank_lst=[]
    for i in range(0,len(ary)):
        key=ary[i]

        idx=sort_lst.index(key)+1
        rank_lst.append(idx)
    return rank_lst

def main():

    ary=[40,10,20,30]
    print(LeetCode1331(ary))

    ary = [100,100,100]
    print(LeetCode1331(ary))

    ary = [37,12,28,9,100,56,80,5,12]
    print(LeetCode1331(ary))

if __name__=='__main__':
    main()