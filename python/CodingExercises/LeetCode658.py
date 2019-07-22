'''
658. Find K Closest Elements
Medium
Given a sorted array, two integers k and x, find the k closest elements to x in the array.
The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.
Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
'''

def LeetCode658(ary, k, x):

    lst=[]
    for i in range(0,len(ary)):
        key=ary[i]
        diff=key-x
        tup=(key,diff)
        lst.append(tup)
    sort_lst=sorted(lst,key=lambda x:x[1])
    fnl_lst=[]
    i=0
    while i<k:
        fnl_lst.append(sort_lst[i][0])
        i=i+1
    return fnl_lst

def main():

    ary=[1,2,3,4,5]
    k=4
    x=3
    print(LeetCode658(ary,k,x))

    ary = [1, 2, 3, 4, 5]
    k = 4
    x = -1
    print(LeetCode658(ary, k, x))

if __name__=='__main__':
    main()