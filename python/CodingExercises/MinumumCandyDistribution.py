'''
https://www.codingeek.com/practice-examples/interview-programming-problems/minimum-candy-distribution-interview-algorithm-problem/
So the problem statement is –
A teacher has some students in class.
She has to distribute some candies to these students.
Every student has some grades/rank that he/she has acquired over a series of tests.
Now students are sitting in a line in a random order(will be provided in input) and there are few rules that teacher has to follow while distributing the candies.
Rules are –
Among any two students who sit adjacent to each other and have different grades, student with the higher grades must get extra candies.
At least one candy is given to every student.
Students sitting adjacent to each other and have same grades then there is no condition on the number of candies they get
i.e. if one get 5 candies other can get 15 or even 1 or 5 or any other positive number(but we have to minimize this).
There might be other conditions on the input but for now, we will focus on the logic on how to do this –
'''

def MinimumCandyDistribution(ary):

    lst=[0]*len(ary)

    lst[0]=1
    for i in range(1,len(ary)):

        if lst[i]==0:
            lst[i]=1
        if ary[i]>ary[i-1]:
            lst[i]=lst[i-1]+1

    for i in range(len(ary)-1,-1,-1):

        if ary[i-1]>ary[i]:
            lst[i-1]=lst[i]+1

    sum=0
    for l in lst:
        sum=sum+l

    return sum

def main():

    ary=[2, 3, 4, 4, 3, 2, 1]
    print(MinimumCandyDistribution(ary))

if __name__=='__main__':
    main()