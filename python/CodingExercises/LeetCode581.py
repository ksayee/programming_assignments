'''
581. Shortest Unsorted Continuous Subarray
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
'''

def LeetCode581(ary):

    start=0
    end=0
    for i in range(0,len(ary)-1):
        if ary[i]>ary[i+1]:
            break
    start=i
    for j in range(len(ary)-1,-1,-1):
        if ary[j]<ary[j-1]:
            break
    end=j

    min=999
    max=-999
    for k in range(start,end+1):
        if ary[k]<min:
            min=ary[k]
        if ary[k]>max:
            max=ary[k]

    for i in range(0,start+1):
        if ary[i]<min:
            continue
        else:
            start=i
            break

    for j in range(end+1,len(ary)):
        if ary[j]>max:
            continue
        else:
            end=j
            break

    return ary[start:end+1]

def main():

    ary=[2, 6, 4, 8, 10, 9, 15]
    print(LeetCode581(ary))

    ary = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
    print(LeetCode581(ary))

    ary = [0, 1, 15, 25, 6, 7, 30, 40, 50]
    print(LeetCode581(ary))

if __name__=='__main__':
    main()