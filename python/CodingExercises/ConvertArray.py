# Convert an array to reduced form | Set 1 (Simple and Hashing)
# Given an array with n distinct elements, convert the given array to a form where all elements are in range from 0 to n-1.
# The order of elements is same, i.e., 0 is placed in place of smallest element, 1 is placed for second smallest element, … n-1 is placed for largest element.

def ConvertArray(ary):

    lst=sorted(ary)

    fnl_lst=[]

    for l in ary:
        idx=lst.index(l)
        fnl_lst.append(idx)

    return fnl_lst

def main():
    
    ary=[10, 40, 20]
    print(ConvertArray(ary))

    ary = [5, 10, 40, 30, 20]
    print(ConvertArray(ary))

if __name__=='__main__':
    main()