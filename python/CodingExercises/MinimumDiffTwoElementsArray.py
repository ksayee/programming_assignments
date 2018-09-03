# Find minimum difference between any two elements
# Given an unsorted array, find the minimum difference between any pair in given array.

def MinimumDiffTwoElementsArray(ary):

    ary.sort()

    min=999

    for i  in range(1,len(ary)):
        if ary[i]-ary[i-1]<min:
            min=ary[i]-ary[i-1]
    return min

def main():

    ary=[1, 5, 3, 19, 18, 25]
    print(MinimumDiffTwoElementsArray(ary))

    ary = [30, 5, 20, 9]
    print(MinimumDiffTwoElementsArray(ary))

    ary = [1, 19, -4, 31, 38, 25, 100]
    print(MinimumDiffTwoElementsArray(ary))

if __name__=='__main__':
    main()