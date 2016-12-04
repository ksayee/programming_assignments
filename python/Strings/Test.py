#Program to add a single number until we reach single digit
#eg: 38: 3+8=11: 1+1=2
def maxprofit(ary):

    max=-9999
    for i in range(0,len(ary)):
        for j in range(i+1,len(ary)):
            num=ary[j]-ary[i]
            if i==0 and j==0:
                max=num
            elif num>max:
                max=num

    print(max)

def multiply(ary):

    left=[1]*len(ary)
    right=[1]*len(ary)
    prod=[1]*len(ary)

    for i in range(1,len(ary)):
        left[i]=ary[i-1]*left[i-1]

    for i in range(len(ary)-2,-1,-1):
        right[i]=ary[i+1]*right[i+1]

    for i in range(0,len(ary)):
        prod[i]=left[i]*right[i]

    print(prod)

def binsrch(ary,n):

    left=0
    right=len(ary)-1
    mid=int((left+right+1)/2)

    while n!=ary[mid]:
        if n<ary[mid]:
            right=mid-1
        else:
            left=mid+1
        mid = int((left + right+1) / 2)

    print(mid)



def main():
    #ary=[12,11,15,3,10]
    #maxprofit(ary)

    #ary=[1,2,3,4]
    #multiply(ary)

    ary=[1,3,4,6,7,34,45,78]
    n=34
    binsrch(ary,n)

if __name__=='__main__':
    main()