'''
Given an array and a value, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
Example:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
'''

def RemoveElement(lst,val):

    ln=len(lst)
    i=0
    while(i<ln):
        if lst[i]==val:
            del lst[i]
            ln=ln-1
        i=i+1
    print(lst)
    return len(lst)

def main():

    lst=[3,2,2,3]
    val=3
    print(RemoveElement(lst,val))

    lst=[3,2,2,3,4,3,2,2,2,5,2]
    val=2
    print(RemoveElement(lst,val))

if __name__=='__main__':
    main()
