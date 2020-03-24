'''
This problem was asked by Palantir.
Write a program that checks whether an integer is a palindrome.
For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert the integer into a string.
'''

def DailyCodingProblem491(num):

    tmp=num
    new_num=0
    i=1
    ary=[]
    while tmp!=0:
        rem=tmp%10
        ary.append(rem)
        tmp=tmp//10
    while len(ary)>0:
        new_num=new_num+ary[-1]*i
        ary.pop()
        i=i*10
    if new_num==num:
        return True
    return False

def main():

    num=121
    print(DailyCodingProblem491(num))

    num = 888
    print(DailyCodingProblem491(num))

    num = 678
    print(DailyCodingProblem491(num))

if __name__=='__main__':
    main()