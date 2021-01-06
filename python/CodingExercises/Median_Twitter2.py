'''
The median of a set of integers is the midpoint value of the data set for
which an equal number of integers are less than and greater than the value.
Given a streaming list of integers between 0 and 100, find the median. For example,


Input: 1,2,3,4,5
Output: 3
Input: 1,2,3,4,5,6
Output: 3.5

'''

def solution1(lst):

    if len(lst)%2!=0:
        mid=int(len(lst)/2)
        return lst[mid]
    else:
        mid1=int(len(lst)/2)
        mid2=int(len(lst)/2)-1
        return (lst[mid1]+lst[mid2])/2

def main():
    
    lst=[1,2,3,4,5]
    print(solution1(lst))

    lst = [1,2,3,4,5,6]
    print(solution1(lst))

if __name__=='__main__':
    main()