'''
1122. Relative Sort Array
Easy
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.
Example 1:
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
'''

import collections
def LeetCode1122(arr1,arr2):

    lst=[]
    dict=collections.Counter(arr1)

    for i in range(0,len(arr2)):
        key=arr2[i]
        if key in dict.keys():
            cnt=dict.get(key)
            k=0
            while k<cnt:
                lst.append(key)
                k=k+1
    for i in range(0,len(arr1)):
        if arr1[i] not in arr2:
            lst.append(arr1[i])
    return lst
def main():

    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    print(LeetCode1122(arr1,arr2))

if __name__=='__main__':
    main()