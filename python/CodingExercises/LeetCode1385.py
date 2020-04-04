'''
1385. Find the Distance Value Between Two Arrays
Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.
The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
Example 1:
Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation:
For arr1[0]=4 we have:
|4-10|=6 > d=2
|4-9|=5 > d=2
|4-1|=3 > d=2
|4-8|=4 > d=2
For arr1[1]=5 we have:
|5-10|=5 > d=2
|5-9|=4 > d=2
|5-1|=4 > d=2
|5-8|=3 > d=2
For arr1[2]=8 we have:
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2
Example 2:
Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
Output: 2
Example 3:
Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
Output: 1
'''

import math
def LeetCode1385(arr1,arr2,d):

    cnt=0
    for num1 in arr1:
        flg=True
        for num2 in arr2:
            if abs(num1-num2)>d:
                pass
            else:
                flg=False
                break
        if flg==True:
            cnt=cnt+1
    return cnt

def main():
    arr1 = [4, 5, 8]
    arr2 = [10, 9, 1, 8]
    d=2
    print(LeetCode1385(arr1,arr2,d))

    arr1 = [1,4,2,3]
    arr2 = [-4,-3,6,10,20,30]
    d = 3
    print(LeetCode1385(arr1, arr2, d))

    arr1 = [2,1,100,3]
    arr2 = [-5,-2,10,-3,7]
    d = 6
    print(LeetCode1385(arr1, arr2, d))

if __name__=='__main__':
    main()