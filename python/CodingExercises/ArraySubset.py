# Find whether an array is subset of another array | Added Method 3
# Given two arrays: arr1[0..m-1] and arr2[0..n-1]. Find whether arr2[] is a subset of arr1[] or not. Both the arrays are not in sorted order. It may be assumed that elements in both array are distinct.
# Examples:
# Input: arr1[] = {11, 1, 13, 21, 3, 7}, arr2[] = {11, 3, 7, 1}
# Output: arr2[] is a subset of arr1[]
# Input: arr1[] = {1, 2, 3, 4, 5, 6}, arr2[] = {1, 2, 4}
# Output: arr2[] is a subset of arr1[]

def ArraySubset(ary1,ary2):

    flg=True

    if len(ary1)>len(ary2):
        sml_ary=ary2
        big_ary=ary1
    else:
        sml_ary=ary1
        big_ary=ary2

    for l in sml_ary:
        if l not in big_ary:
            flg=False

    if flg==True:
        return "Small array is subset of Big array"
    else:
        return "Small array is NOT subset of Big Array"

def main():
    
    ary1=[11, 1, 13, 21, 3, 7]
    ary2=[11, 3, 7, 1]
    print(ArraySubset(ary1,ary2))

    ary1 = [1, 2, 3, 4, 5, 6]
    ary2 = [1, 2, 4]
    print(ArraySubset(ary1, ary2))

    ary1 = [10, 5, 2, 23, 19]
    ary2 = [19, 5, 3]
    print(ArraySubset(ary1, ary2))

if __name__=='__main__':
    main()