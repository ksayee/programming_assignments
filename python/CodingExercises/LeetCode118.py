'''
118. Pascal's Triangle
Easy
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

def LeetCode118(num):

    lst=[]
    lst.append([1])
    lst.append([1,1])

    k=2
    while k<num:
        tmp=[]
        tmp.append(1)
        for i in range(1,len(lst[-1])):
            tmp.append(lst[-1][i-1]+lst[-1][i])
        tmp.append(1)
        lst.append(tmp.copy())
        k=k+1
    return lst

def main():

    num=5
    print(LeetCode118(num))

    num = 7
    print(LeetCode118(num))

if __name__=='__main__':
    main()