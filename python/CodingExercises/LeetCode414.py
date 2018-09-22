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

    first=ary[0]
    second=-9999
    third=-9999

    for i in range(1,len(ary)):
        key=ary[i]
        if key>first:
            third=second
            second=first
            first=key
        elif key>second:
            if key==first:
                continue
            else:
                third=second
                second=key
        elif key>third:
            if key==second:
                continue
            else:
                third=key


    if third==-9999:
        return first
    else:
        return third

def main():

    ary=[3, 2, 1]
    print(LeetCode414(ary))

    ary = [1, 2]
    print(LeetCode414(ary))

    ary = [2,2, 3, 1]
    print(LeetCode414(ary))

if __name__=='__main__':
    main()