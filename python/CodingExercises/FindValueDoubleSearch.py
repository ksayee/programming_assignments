# Find final value if we double after every successful search in array
# Given an array and an integer k,
# traverse the array and if the element in array is k, double the value of k and continue traversal.
# In the end return value of k.

def FindValueDoubleSearch(ary,k):

    while True:

        if k in ary:
            k=k*2
        else:
            break

    return k

def main():

    ary=[2, 3, 4, 10, 8, 1]
    k=2
    print(FindValueDoubleSearch(ary,k))

    ary = [2, 4, 5, 6, 7]
    k = 3
    print(FindValueDoubleSearch(ary, k))

if __name__=='__main__':
    main()