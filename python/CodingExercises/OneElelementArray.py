# Find the element that appears once in an array where every other element appears twice
# Given an array of integers.
# All numbers occur twice except one number which occurs once. Find the number in O(n) time & constant extra space.
# The best solution is to use XOR. XOR of all array elements gives us the number with single occurrence.
# The idea is based on following two facts.
# a) XOR of a number with itself is 0.
# b) XOR of a number with 0 is number itself.

def OneElementArray(ary):

    rem=0

    for i in range(0,len(ary)):

        rem=rem ^ ary[i]

    return rem

def main():
    
    ary=[7, 3, 5, 4, 5, 3, 4]
    print(OneElementArray(ary))

if __name__=='__main__':
    main()