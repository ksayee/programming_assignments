'''
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
Example:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
'''

def RemoveDuplicates(lst):

    if len(lst)==0:
        return 0
    elif len(lst)==1:
        return 1

    j=1
    for i in range(1,len(lst)):
        if lst[i]!=lst[i-1]:
            lst[j]=lst[i]
            j=j+1
    return j

def main():
    lst=[]
    print(RemoveDuplicates(lst))

    lst=[1]
    print(RemoveDuplicates(lst))

    lst=[1,1,2]
    print(RemoveDuplicates(lst))

    lst = [1, 1, 2,2,2,2,4,5,5,5,6,6]
    print(RemoveDuplicates(lst))

if __name__=='__main__':
    main()
