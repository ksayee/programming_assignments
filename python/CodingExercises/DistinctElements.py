# Print All Distinct Elements of a given integer array
# Given an integer array, print all distinct elements in array.
# The given array may contain duplicates and the output should print every element only once.
# The given array is not sorted.

def DistinctElements(ary):

    fnl_lst=[]

    for i in range(0,len(ary)):

        key=ary[i]

        if key not in fnl_lst:
            fnl_lst.append(key)

    return fnl_lst
    
def main():
    
    ary=[12, 10, 9, 45, 2, 10, 10, 45]
    print(DistinctElements(ary))

    ary = [1, 2, 3, 4, 5]
    print(DistinctElements(ary))

    ary = [1, 1, 1, 1, 1]
    print(DistinctElements(ary))

if __name__=='__main__':
    main()