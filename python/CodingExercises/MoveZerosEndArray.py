# Move all zeroes to end of array
# Given an array of random numbers, Push all the zero’s of a given array to the end of the array.
# For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}.
# The order of all other elements should be same. Expected time complexity is O(n) and extra space is O(1).

def MoveZerosEndArray(ary):

    cnt=0

    for i in range(0,len(ary)):

        if ary[i]!=0:
            ary[cnt]=ary[i]
            cnt=cnt+1

    while cnt<len(ary):
        ary[cnt]=0
        cnt=cnt+1
    return ary

def main():

    ary=[1, 2, 0, 4, 3, 0, 5, 0]
    print(MoveZerosEndArray(ary))

    ary = [1, 2, 0, 0, 0, 3, 6]
    print(MoveZerosEndArray(ary))

    ary = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
    print(MoveZerosEndArray(ary))

if __name__=='__main__':
    main()