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

def reversenum(num):
    lst=[]

    neg_flg=False
    if num<0:
        num=num*(-1)
        neg_flg=True

    while num!=0:
        lst.append(str(num%10))
        num=int(num/10)

    if neg_flg==True:
        print(int(''.join(lst))*-1)
    else:
        print(''.join(lst))

def secondmax(ary):

    for i in range(0,len(ary)):
        if i==0:
            max=ary[i]
        elif ary[i]<max:
            if i==1:
                sec_max=ary[i]
            elif sec_max>ary[i]:
                sec_max=ary[i]
        elif ary[i]>max:
            sec_max=max
            max=ary[i]

    print(max)
    print(sec_max)

def sumofnum(ary):

    for i in range(0,len(ary)):
        if i==0:
            max=ary[i]
        elif ary[i]<max:
            if i==1:
                sec_max=ary[i]
            elif sec_max>ary[i]:
                sec_max=ary[i]
        elif ary[i]>max:
            sec_max=max
            max=ary[i]

    print(max)
    print(sec_max)

def numsum(num):

    while num>10:
        sum=0
        while num!=0:
            sum=sum+num%10
            num=int(num/10)
        if sum>9:
            num=sum

    print(sum)


def groupanagrams(ary):

    lst={}

    for i in range(0,len(ary)):
        key=''.join(sorted(ary[i]))
        if key in lst.keys():
            lst[key].append(ary[i])
        else:
            lst[key]=[]
            lst[key].append(ary[i])

    for key,val in lst.items():
        print(val)

def main():
    #ary=[12,11,15,3,10]
    #maxprofit(ary)

    #ary=[1,2,3,4]
    #multiply(ary)

    #ary=[1,3,4,6,7,34,45,78]
    #n=34
    #binsrch(ary,n)

    #num=-1234
    #reversenum(num)

    #ary=[3,4,8,1,5,-2,43]
    #secondmax(ary)

    #num=87459
    #numsum(num)

    ary = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    groupanagrams(ary)

if __name__=='__main__':
    main()