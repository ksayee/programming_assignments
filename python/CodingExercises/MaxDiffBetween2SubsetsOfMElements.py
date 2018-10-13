'''
Maximum difference between two subsets of m elements
Given an array of n integers and a number m, find the maximum possible difference between two sets of m elements chosen from given array.

Examples:

Input : arr[] = 1 2 3 4 5
            m = 4
Output : 4
The maximum four elements are 2, 3,
4 and 5. The minimum four elements are
1, 2, 3 and 4. The difference between
two sums is (2 + 3 + 4 + 5) - (1 + 2
+ 3 + 4) = 4

Input : arr[] = 5 8 11 40 15
           m = 2
Output : 42
The difference is (40 + 15) - (5  + 8)
'''

def MaxDiffBetween2SubsetsOfMElements(ary,m):

    left=0
    right=len(ary)-1
    ary.sort()

    j=0
    min_sum=0
    max_sum=0
    while j<m:

        min_sum=min_sum+ary[left]
        max_sum=max_sum+ary[right]
        j=j+1
        left=left+1
        right=right-1

    return max_sum-min_sum

def main():

    ary=[1,2,3,4,5]
    m=4
    print(MaxDiffBetween2SubsetsOfMElements(ary,m))

    ary = [5,8,11,40,15]
    m=2
    print(MaxDiffBetween2SubsetsOfMElements(ary,m))

if __name__=='__main__':
    main()