'''
414. Third Maximum Number
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''

def LeetCode414(ary):

    cnt=1
    tmp_max=-999
    max=-999

    for i in range(0,len(ary)):
        key=ary[i]
        if i==0:
            max=key
            tmp_max=key
        else:
            if key<=tmp_max and cnt<=3:
                tmp_max=key
                cnt=cnt+1
            if key>max:
                max=key

    if cnt==3:
        return tmp_max
    else:
        return max
def main():

    ary=[3, 2, 1]
    print(LeetCode414(ary))

    ary = [1, 2]
    print(LeetCode414(ary))

    ary = [2, 2, 3, 1]
    print(LeetCode414(ary))

if __name__=='__main__':
    main()