
def reversearray(ary):

    left=0
    right=len(ary)-1

    for i in range(0,len(ary)-1):
        if left<right:
            temp=ary[right]
            ary[right]=ary[left]
            ary[left]=temp
            left=left+1
            right=right-1

    print(ary)

def main():

    ary=[1,2,3,4,5,6]
    reversearray(ary)


if __name__=='__main__':
    main()
