'''
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''


def LeetCode42(ary):

    l=0
    r=len(ary)-1
    water=0
    l_max=0
    r_max=0

    while l<r:

        if ary[l]<ary[r]:
            if ary[l]>l_max:
                l_max=ary[l]
            else:
                water=water+l_max-ary[l]
            l=l+1
        else:
            if ary[r]>r_max:
                r_max=ary[r]
            else:
                water=water+r_max-ary[r]
            r=r-1

    return water

def main():
    
    ary=[0,1,0,2,1,0,1,3,2,1,2,1]
    print(LeetCode42(ary))

if __name__=='__main__':
    main()