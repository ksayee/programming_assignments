'''
373. Find K Pairs with Smallest Sums
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence:
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence:
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
'''

def LeetCode373(num1, num2, k):

    dict={}
    for n1 in num1:
        for n2 in num2:
            sum=n1+n2
            if sum in dict.keys():
                tmp=(n1,n2)
                dict[sum].append(tmp)
            else:
                tmp=[]
                tup=(n1,n2)
                tmp.append(tup)
                dict[sum]=tmp
    res_lst=sorted(dict.items(),key=lambda x:x[1])
    idx=0
    i=0
    fnl_lst=[]
    while i<k:
        lst=res_lst[idx]
        for l in lst[1]:
            if l not in fnl_lst:
                fnl_lst.append(l)
            i=i+1
        if idx<len(res_lst)-1:
            idx=idx+1

    return fnl_lst

def main():

    num1=[1,7,11]
    num2=[2,4,6]
    k=3
    print(LeetCode373(num1,num2,k))

    num1 = [1,1,2]
    num2 = [1,2,3]
    k = 2
    print(LeetCode373(num1, num2, k))

    num1 = [1,2]
    num2 = [3]
    k = 3
    print(LeetCode373(num1, num2, k))

if __name__=='__main__':
    main()