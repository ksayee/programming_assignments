# String slicing in Python to rotate a string
# Given a string of size n, write functions to perform following operations on string.
# Left (Or anticlockwise) rotate the given string by d elements (where d <= n).
# Right (Or clockwise) rotate the given string by d elements (where d <= n).

def SlicingRotate(str,n):

    lst=list(str)

    l_lst=lst[n:]+lst[0:n]
    r_lst=lst[len(str)-n:]+lst[0:len(str)-n]
    print("Left Rotate:",''.join(l_lst))
    print("Right Rotate:",''.join(r_lst))

def main():

    str='GeeksforGeeks'
    n=2
    SlicingRotate(str,2)

    str = 'qwertyu'
    n = 2
    SlicingRotate(str, 2)

if __name__=='__main__':
    main()