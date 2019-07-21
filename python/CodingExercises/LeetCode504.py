'''
504. Base 7
Easy
Given an integer, return its base 7 string representation.
Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
'''

def LeetCode504(num):

    lst=[]
    if num<0:
        neg_flg=True
        num=-1*num
    else:
        neg_flg=False

    while num!=0:
        rem=num%7
        num=num//7
        lst.append(str(rem))
    lst.reverse()
    if neg_flg==True:
        return -1*int(''.join(lst))
    else:
        return int(''.join(lst))

def main():

    num=100
    print(LeetCode504(num))

    num =-7
    print(LeetCode504(num))

if __name__=='__main__':
    main()