'''
944. Delete Columns to Make Sorted
Easy
We are given an array A of N lowercase letter strings, all of the same length.
Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.
For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then
the final array after deletions is ["bef", "vyz"], and the remaining columns of A are ["b","v"], ["e","y"], and ["f","z"].
(Formally, the c-th column is [A[0][c], A[1][c], ..., A[A.length-1][c]].)
Suppose we chose a set of deletion indices D such that after deletions, each remaining column in A is in non-decreasing sorted order.
Return the minimum possible value of D.length.
Example 1:
Input: ["cba","daf","ghi"]
Output: 1
Explanation:
After choosing D = {1}, each column ["c","d","g"] and ["a","f","i"] are in non-decreasing sorted order.
If we chose D = {}, then a column ["b","a","h"] would not be in non-decreasing sorted order.
Example 2:
Input: ["a","b"]
Output: 0
Explanation: D = {}
Example 3:
Input: ["zyx","wvu","tsr"]
Output: 3
Explanation: D = {0, 1, 2}
'''

def LeetCode944(ary):

    deleted=[]
    word=ary[0]
    for i in range(1,len(ary)):
        key=ary[i]
        for k in range(0,len(key)):
            if word[k]<key[k]:
                pass
            else:
                if k not in deleted:
                    deleted.append(k)
        word=key
    return len(deleted)

def main():

    ary = ["cba","daf","ghi"]
    print(LeetCode944(ary))

    ary = ["a","b"]
    print(LeetCode944(ary))

    ary = ["zyx","wvu","tsr"]
    print(LeetCode944(ary))

if __name__=='__main__':
    main()