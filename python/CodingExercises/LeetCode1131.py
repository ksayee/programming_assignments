'''
1131. Maximum of Absolute Value Expression
Medium
Given two arrays of integers with equal lengths, return the maximum value of:
|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
where the maximum is taken over all 0 <= i, j < arr1.length.
Example 1:
Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
Output: 13
Example 2:
Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
Output: 20
'''

def LeetCode1131(arr1,arr2):

    fnl_lst=[]
    for i in range(0,len(arr1)):
        for j in range(0,len(arr2)):
            sum=abs(arr1[i]-arr1[j])+abs(arr2[i]-arr2[j])+abs(i-j)
            fnl_lst.append(sum)
    return sorted(fnl_lst,reverse=True)[0]

def main():

    arr1 = [1, 2, 3, 4]
    arr2 = [-1, 4, 5, 6]
    print(LeetCode1131(arr1,arr2))

    arr1 = [1,-2,-5,0,10]
    arr2 = [0,-2,-1,-7,-4]
    print(LeetCode1131(arr1, arr2))

if __name__=='__main__':
    main()