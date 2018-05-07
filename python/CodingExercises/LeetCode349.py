'''
349. Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
'''


def intersection(nums1, nums2):
    if len(nums1) <= len(nums2):
        sml_ary = nums1
        big_ary = nums2
    else:
        sml_ary = nums2
        big_ary = nums1

    fnl = []
    for i in range(0, len(sml_ary)):
        if sml_ary[i] in big_ary and sml_ary[i] not in fnl:
            fnl.append(sml_ary[i])
    return fnl

def main():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(intersection(nums1, nums2))

if __name__=='__main__':
    main()