# Write a program to reverse an array or string
# Given an array (or string), the task is to reverse the array/string.

def ReverseArray(ary,st,end):

    if st<=end:
        tmp=ary[st]
        ary[st]=ary[end]
        ary[end]=tmp
        ReverseArray(ary,st+1,end-1)
    return ary

def main():

    ary=[1, 2, 3]
    print(ReverseArray(ary,0,len(ary)-1))

    ary = [4, 5, 1, 2]
    print(ReverseArray(ary, 0, len(ary) - 1))

if __name__=='__main__':
    main()