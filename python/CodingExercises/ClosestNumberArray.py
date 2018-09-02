# Find closest number in array
# Given an array of sorted integers.
# We need to find the closest value to the given number.
# Array may contain duplicate values and negative numbers.

def ClosestNumberArray(ary,k):

    dict={}

    for i in range(0,len(ary)):

        diff=abs(k-ary[i])

        if diff not in dict.keys():
            dict[diff]=ary[i]

    min=999

    result=0
    for key, val in dict.items():

        if key<min:
            min=key
            result=val

    return result

def main():

    ary=[1, 2, 4, 5, 6, 6, 8, 9]
    k=11
    print(ClosestNumberArray(ary,k))

    ary = [2, 5, 6, 7, 8, 8, 9]
    k = 4
    print(ClosestNumberArray(ary,k))

if __name__=='__main__':
    main()