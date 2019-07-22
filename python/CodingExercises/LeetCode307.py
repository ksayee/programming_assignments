'''
307. Range Sum Query - Mutable
Medium
Share
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]
sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
'''

def update(ary,idx,val):

    try:
        ary[idx]=val
    except:
        pass

def sumRange(ary,left,right):

    sum=0
    k=left
    while k<=right:
        sum=sum+ary[k]
        k=k+1
    return sum

def main():

    ary=[1, 3, 5]
    print(sumRange(ary,0,2))
    update(ary,1, 2)
    print(sumRange(ary,0, 2))
    
if __name__=='__main__':
    main()