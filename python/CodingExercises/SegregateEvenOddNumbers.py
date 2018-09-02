# Segregate Even and Odd numbers
# Given an array A[], write a function that segregates even and odd numbers.
# The functions should put all even numbers first, and then odd numbers.

def SegregateEvenOddNumbers(ary):

    l=0
    h=len(ary)-1

    while l<h:

        while ary[l]%2==0 and l<h:
            l=l+1
        while ary[h]%2==1 and l<h:
            h=h-1

        if l<h:
            tmp=ary[h]
            ary[h]=ary[l]
            ary[l]=tmp

    return ary


def main():

    ary=[12, 34, 45, 9, 8, 90, 3]
    print(SegregateEvenOddNumbers(ary))

    ary = [1,9,5,3,2,6,7,11]
    print(SegregateEvenOddNumbers(ary))

    ary = [1,3,2,4,7,6,9,10]
    print(SegregateEvenOddNumbers(ary))

if __name__=='__main__':
    main()