'''
Distributing all balls without repetition
Given N balls. For convenience, we denote color of each ball as — lowercase letter. We have to distribute N balls among K people. They will be upset, if they get two balls of the same color. We can give any number of balls to people and they won’t be upset even if they do not get any ball, but, we have to distribute all balls, such that no one will be upset — print YES, if it is possible , and NO, otherwise.

Examples:

Input : 4 2 // value of N and K
        aabb // colors of given balls
Output : YES
We can give 1st and 3rd ball to the first person,
and 2nd and 4th to the second.

Input : 6 3 // value of N and K
        aacaab // colors of given balls
Output : NO
We need to give all balls of color a, but one
ball will stay, that's why answer is NO
'''

def DistributeBallsWithoutRepetition(str1, balls):

    lst=[0]*26

    for i in range(0,len(str1)):
        key=str1[i]
        lst[ord(key)-ord('a')]=lst[ord(key)-ord('a')]+1

    for i in range(0,len(lst)):
        if lst[i]!=0:
            if lst[i]>balls:
                return False
    return True

def main():

    str1='aabb'
    balls=2
    print(DistributeBallsWithoutRepetition(str1,balls))

    str1 = 'aacaab'
    balls = 3
    print(DistributeBallsWithoutRepetition(str1, balls))

if __name__=='__main__':
    main()