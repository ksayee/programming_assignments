'''
896. Monotonic Array

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.
Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true
'''

def LeetCode896(ary):

    flg1=True
    flg2=True

    for i in range(1,len(ary)):
        if ary[i]>=ary[i-1]:
            continue
        else:
            flg1=False
            break

    for i in range(1,len(ary)):
        if ary[i]<=ary[i-1]:
            continue
        else:
            flg2=False
            break


    if flg1==False and flg2==False:
        return False
    else:
        return True

def main():
    
    ary= [1,2,2,3]
    print(LeetCode896(ary))

    ary = [6,5,4,4]
    print(LeetCode896(ary))

    ary = [1,3,2]
    print(LeetCode896(ary))

    ary = [1,2,4,5]
    print(LeetCode896(ary))

    ary = [1,1,1]
    print(LeetCode896(ary))

if __name__=='__main__':
    main()