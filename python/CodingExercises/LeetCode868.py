'''
868. Binary Gap

Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.

If there aren't two consecutive 1's, return 0.



Example 1:

Input: 22
Output: 2
Explanation:
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.
Example 2:

Input: 5
Output: 2
Explanation:
5 in binary is 0b101.
Example 3:

Input: 6
Output: 1
Explanation:
6 in binary is 0b110.
Example 4:

Input: 8
Output: 0
Explanation:
8 in binary is 0b1000.
There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.

'''

def LeetCode868(str1):

    lst=list(str1)
    flg=False
    max=-1
    cnt=0
    for i in range(0,len(lst)):

        key=lst[i]

        if flg==False and key=='0':
            continue
        elif key=='0' and flg==True:
            cnt=cnt+1
        elif key=='1':
            if flg==False:
                cnt=1
                flg=True
            elif flg==True:
                if cnt>max:
                    max=cnt
                cnt=1
    return max

def main():

    str1='00010110'
    print(LeetCode868(str1))

    str1 = '00000110'
    print(LeetCode868(str1))

    str1 = '00001000'
    print(LeetCode868(str1))

    str1 = '00001001'
    print(LeetCode868(str1))

    str1 = '00100001'
    print(LeetCode868(str1))

    str1 = '11010001'
    print(LeetCode868(str1))

if __name__=='__main__':
    main()