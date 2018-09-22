'''
624. Maximum Distance in Arrays

Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.

Example 1:
Input:
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation:
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Note:
Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].
'''

def LeetCode624(ary):

    first_val=ary[0][0]
    last_val=ary[0][len(ary[0])-1]
    max_val=-999
    tmp=[]

    for i in range(1,len(ary)):
        tmp=[]
        first_val_1=ary[i][0]
        last_val_1=ary[i][len(ary[i])-1]

        val_1=abs(first_val-first_val_1)
        tmp.append(val_1)
        val_2=abs(first_val-last_val_1)
        tmp.append(val_2)
        val_3=abs(last_val-first_val_1)
        tmp.append(val_3)
        val_4=abs(last_val-last_val_1)
        tmp.append(val_4)
        key=sorted(tmp,reverse=True)[0]

        if key>max_val:
            if key==val_1:
                first_val=first_val
                last_val=first_val_1
            elif key==val_2:
                first_val = first_val
                last_val=last_val_1
            elif key==val_3:
                first_val=first_val_1
                last_val=last_val
            elif key==val_4:
                first_val=last_val_1
                last_val=last_val
            max_val=key

    return max_val

def main():

    ary=[[1,2,3],[4,5],[1,2,3]]
    print(LeetCode624(ary))

if __name__=='__main__':
    main()