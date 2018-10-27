'''
Good morning! Here's your coding interview problem for today.
This problem was asked by Facebook.
You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is
 unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.
Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in
 the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
'''

def DailyCodingProblem30(ary):

    water=0
    left=0
    right=len(ary)-1
    left_max=0
    right_max=0

    while left <=right:

        if ary[left]<ary[right]:

            if ary[left]>left_max:
                left_max=ary[left]
            else:
                water=water+left_max-ary[left]
            left=left+1
        else:
            if ary[right]>right_max:
                right_max=ary[right]
            else:
                water=water+right_max-ary[right]
            right=right-1
    return water

def main():

    ary=[3, 0, 1, 3, 0, 5]
    print(DailyCodingProblem30(ary))

    ary = [2, 1, 2]
    print(DailyCodingProblem30(ary))

if __name__=='__main__':
    main()