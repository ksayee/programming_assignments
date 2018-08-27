# Minimum delete operations to make all elements of array same
# Given an array of n elements such that elements may repeat.
# We can delete any number of elements from array. The task is to find minimum number of elements to be deleted from array to make it equal.

def MinimumDelete(ary):

    dict={}

    for l in ary:

        if l in dict.keys():
            dict[l]=dict.get(l)+1
        else:
            dict[l]=1

    max_val=0

    for key,val in dict.items():
        if val>max_val:
            max_val=val

    return len(ary)-max_val

def main():

    ary=[4, 3, 4, 4, 2, 4]
    print(MinimumDelete(ary))

    ary = [1, 2, 3, 4, 5]
    print(MinimumDelete(ary))

if __name__=='__main__':
    main()