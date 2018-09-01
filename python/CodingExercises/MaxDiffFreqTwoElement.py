# Maximum difference between frequency of two elements such that element having greater frequency is also greater
# Given an array of n positive integers with many repeating elements.
# The task is to find maximum difference between the frequency of any two different elements,
# such that the element with greater frequency is also greater in value than the second integer.

def MaxDiffFreqTwoElement(ary):

    dict={}

    for l in ary:
        if l in dict.keys():
            dict[l]=dict.get(l)+1
        else:
            dict[l]=1

    min=999
    max=0
    max_key=0
    min_key=0

    for key, val in dict.items():
        if val>max:
            max=val
            max_key=key
        if val<min:
            min=val
            min_key=key

    if max_key>min_key:
        return max_key-min_key
    else:
        return 0

def main():

    ary=[3, 1, 3, 2, 3, 2]
    print(MaxDiffFreqTwoElement(ary))

if __name__=='__main__':
    main()