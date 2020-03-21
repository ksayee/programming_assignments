'''
1351. Count Negative Numbers in a Sorted Matrix
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.
Return the number of negative numbers in grid.
Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:
Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:
Input: grid = [[1,-1],[-1,-1]]
Output: 3
Example 4:
Input: grid = [[-1]]
Output: 1
'''

def LeetCode1351(grid):
    cnt=0
    for i in range(0,len(grid)):
        lst=grid[i]
        for j in range(len(lst)-1,-1,-1):
            if lst[j]<0:
                cnt=cnt+1
            else:
                break
    return cnt

def main():

    grid=[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    print(LeetCode1351(grid))

    grid = [[3,2],[1,0]]
    print(LeetCode1351(grid))

    grid = [[1,-1],[-1,-1]]
    print(LeetCode1351(grid))

    grid = [[-1]]
    print(LeetCode1351(grid))

if __name__=='__main__':
    main()