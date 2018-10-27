'''
This problem was asked by Microsoft.
A number is considered perfect if its digits sum up to exactly 10.
Given a positive integer n, return the n-th perfect number.
For example, given 1, you should return 19. Given 2, you should return 28.
'''

def DailyCodingProblem70(n):

    st=10

    cnt=0
    fnl_lst=[]
    while cnt<n:
        tmp=st
        sum=0
        while tmp!=0:
            rem=tmp%10
            sum=sum+rem
            tmp=tmp//10
        if sum==10:
            cnt=cnt+1
            fnl_lst.append(st)
        st=st+1
    return sorted(fnl_lst,reverse=True)[0]

def main():

    n=1
    print(DailyCodingProblem70(n))

    n = 2
    print(DailyCodingProblem70(n))

if __name__=='__main__':
    main()