# Last duplicate element in a sorted array
# We have a sorted array with duplicate elements and we have to find the index of
# last duplicate element and print index of it and also print the duplicate element.
# If no such element found print a message.

def LastDuplicateElementSortedArray(ary):

    idx=-1

    for i in range(0,len(ary)):

        key=ary[i]

        if key in ary[i+1:] or key in ary[:i]:
            idx=i
        else:
            continue

    return idx

def main():

    ary=[1, 5, 5, 6, 6, 7]
    print(LastDuplicateElementSortedArray(ary))

    ary = [1, 2, 3, 4, 5]
    print(LastDuplicateElementSortedArray(ary))

    ary = [1, 5, 5, 6, 6, 7,7,8,8,9,10,11,12]
    print(LastDuplicateElementSortedArray(ary))

if __name__=='__main__':
    main()