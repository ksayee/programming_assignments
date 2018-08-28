# Double the first element and move zero to end
# Given an array of integers of size n.
# Assume ‘0’ as invalid number and all other as valid number.
# Convert the array in such a way that if next valid number is same as current number,
# double its value and replace the next number with 0. After the modification, rearrange the array such that all 0’s are shifted to the end.

def DoubleFirstElement(ary):

    for i in range(1,len(ary)):
        if ary[i-1]== ary[i]:
            ary[i-1]=ary[i-1]*2
            ary[i]=0

    cnt=0

    for i in range(0,len(ary)):
        if ary[i]!=0:
            ary[cnt]=ary[i]
            cnt=cnt+1

    while cnt<len(ary):
        ary[cnt]=0
        cnt=cnt+1

    return ary

def main():

    ary = [2, 2, 0, 4, 0, 8]
    print(DoubleFirstElement(ary))

    ary = [0, 2, 2, 2, 0, 6, 6, 0, 0, 8]
    print(DoubleFirstElement(ary))

if __name__=='__main__':
    main()