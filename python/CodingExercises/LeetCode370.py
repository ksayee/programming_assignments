'''
370. Range Addition
Assume you have an array of length n initialized with all 0's and are given k update operations.

Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.

Return the modified array after all k operations were executed.

Example:

Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]
Explanation:

Initial state:
[0,0,0,0,0]

After applying operation [1,3,2]:
[0,2,2,2,0]

After applying operation [2,4,3]:
[0,2,5,5,3]

After applying operation [0,2,-2]:
[-2,0,3,5,3]
'''

def LeetCode370(lgt,upd):

    lst=[0]*lgt

    for ary in upd:

        st=ary[0]
        end=ary[1]
        inc=ary[2]

        while st<=end:
            lst[st]=lst[st]+inc
            st=st+1

    return lst

def main():

    lgt = 5
    upd = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
    print(LeetCode370(lgt,upd))

if __name__=='__main__':
    main()