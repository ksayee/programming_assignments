'''
Count ways to reach the n’th stair
There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. Count the number of ways, the person can reach the top.
stairs

Consider the example shown in diagram. The value of n is 3. There are 3 ways to reach the top. The diagram is taken from Easier Fibonacci puzzles

Input: n = 1
Output: 1
There is only one way to climb 1 stair

Input: n = 2
Output: 2
There are two ways: (1, 1) and (2)

Input: n = 4
Output: 5
(1, 1, 1, 1), (1, 1, 2), (2, 1, 1), (1, 2, 1), (2, 2)
'''

def Combinations_recur(lst,tmp,fnl_lst,n):

    if n==0:
        fnl_lst.append(tmp.copy())
        return

    for i in range(0,len(lst)):
        if lst[i]>n:
            break
        tmp.append(lst[i])
        Combinations_recur(lst, tmp, fnl_lst, n-lst[i])
        tmp.pop()

def ClimbingStairs(n):

    lst=[1,2]
    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,tmp,fnl_lst,n)
    return fnl_lst

def main():

    n=1
    print(ClimbingStairs(n))

    n = 2
    print(ClimbingStairs(n))

    n = 3
    print(ClimbingStairs(n))

    n = 4
    print(ClimbingStairs(n))

    n = 5
    print(ClimbingStairs(n))

if __name__=='__main__':
    main()