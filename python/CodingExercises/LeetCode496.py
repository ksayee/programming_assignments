'''
496. Next Greater Element I
Easy
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.
Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
For number 2 in the first array, the next greater number for it in the second array is 3.
For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
'''
def LeetCode496(num1, num2):

    lst=[]
    for i in range(0,len(num1)):
        key=num1[i]
        idx=num2.index(key)
        flg=False
        for j in range(idx+1,len(num2)):
            if num2[j]>key:
                lst.append(num2[j])
                flg=True
                break
        if flg==False:
            lst.append(-1)
    return lst

def main():

    num1 = [4, 1, 2]
    num2 = [1, 3, 4, 2]
    print(LeetCode496(num1,num2))

    num1 = [2, 4]
    num2 = [1, 2, 3, 4]
    print(LeetCode496(num1, num2))

if __name__=='__main__':
    main()