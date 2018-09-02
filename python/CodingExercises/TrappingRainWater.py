# Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
'''
Examples:
Input: arr[]   = {2, 0, 2}
Output: 2
Structure is like below
| |
|_|
We can trap 2 units of water in the middle gap.

Input: arr[]   = {3, 0, 0, 2, 0, 4}
Output: 10
Structure is like below
     |
|    |
|  | |
|__|_|
We can trap "3*2 units" of water between 3 an 2,
"1 unit" on top of bar 2 and "3 units" between 2
and 4.  See below diagram also.

Input: arr[] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
       |
   |   || |
_|_||_||||||
Trap "1 unit" between first 1 and 2, "4 units" between
first 2 and 3 and "1 unit" between second last 1 and last 2
'''

def TrappingRainWater(ary):

    l=0
    h=len(ary)-1

    left_max=0
    right_max=0

    water=0

    while l<=h:

        if ary[l]<ary[h]:
            if ary[l]>left_max:
                left_max=ary[l]
            else:
                water=water+left_max-ary[l]
            l=l+1
        else:
            if ary[h] > right_max:
                right_max = ary[h]
            else:
                water = water + right_max - ary[h]
            h=h-1

    return water

def main():

    ary=[2, 0, 2]
    print(TrappingRainWater(ary))

    ary = [3, 0, 0, 2, 0, 4]
    print(TrappingRainWater(ary))

    ary = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(TrappingRainWater(ary))

if __name__=='__main__':
    main()