'''
Given an initial array arr, every day you produce a new array using the array of the previous day.
On the i-th day, you do the following operations on the array of day i-1 to produce the array of day i:
If an element is smaller than both its left neighbor and its right neighbor, then this element is incremented.
If an element is bigger than both its left neighbor and its right neighbor, then this element is decremented.
The first and last elements never change.
After some days, the array does not change. Return that final array.
Example 1:
Input: arr = [6,2,3,4]
Output: [6,3,3,4]
Explanation:
On the first day, the array is changed from [6,2,3,4] to [6,3,3,4].
No more operations can be done to this array.
Example 2:
Input: arr = [1,6,3,4,3,5]
Output: [1,4,4,4,4,5]
Explanation:
On the first day, the array is changed from [1,6,3,4,3,5] to [1,5,4,3,4,5].
On the second day, the array is changed from [1,5,4,3,4,5] to [1,4,4,4,4,5].
No more operations can be done to this array.
Constraints:
1 <= arr.length <= 100
1 <= arr[i] <= 100
'''

def ChangeArray(ary):

    chg_flg=False
    for i in range(0,len(ary)):
        if i==0 or i==len(ary)-1:
            pass
        else:
            if ary[i]>ary[i+1] and ary[i]>ary[i-1]:
                ary[i]=ary[i]-1
                chg_flg=True
            elif ary[i]<ary[i+1] and ary[i]<ary[i-1]:
                ary[i]=ary[i]+1
                chg_flg = True
            else:
                pass
    return chg_flg

def LeetCode1243(ary):

    chg_flg=True
    while True:
        chg_flg=ChangeArray(ary)
        if chg_flg==True:
            pass
        else:
            break
    return ary

def main():

    ary=[6,2,3,4]
    print(LeetCode1243(ary))

    ary = [1,6,3,4,3,5]
    print(LeetCode1243(ary))

if __name__=='__main__':
    main()