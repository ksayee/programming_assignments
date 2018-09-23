'''
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
'''


def LeetCode43(num1,num2):

    lst1=list(num1)
    lst2=list(num2)

    carry_a=0
    carry_p=0
    fnl_lst=[]
    for i in range(len(lst2)-1,-1,-1):

        n1=int(lst2[i])
        k = len(lst2)-1 - i
        for j in range(len(lst1)-1,-1,-1):

            n2=int(lst1[j])

            if k==0:
                result=n1*n2+carry_a
                rem = result % 10
                fnl_lst.append(str(rem))
                carry_a=int(result/10)
            else:
                result=n1*n2+carry_a
                rem=result%10
                carry_a=int(result/10)

                if k<len(fnl_lst):
                    result_p=int(fnl_lst[k])+rem+carry_p
                else:
                    result_p=rem+carry_p

                carry_p=int(result_p/10)

                if k<len(fnl_lst):
                    fnl_lst[k]=str(result_p%10)
                else:
                    fnl_lst.append(str(result_p%10))

                if k<len(fnl_lst):
                    k=k+1

        if (carry_a+carry_p)>0:
            fnl_lst.append(str(carry_a+carry_p))
        carry_a=0
        carry_p=0

    fnl_lst.reverse()

    return ''.join(fnl_lst)

def main():
    
    num1='123'
    num2='456'
    print(LeetCode43(num1,num2))

    num1 = '2'
    num2 = '3'
    print(LeetCode43(num1, num2))

    num1 = '25'
    num2 = '76'
    print(LeetCode43(num1, num2))

    num1 = '345'
    num2 = '89'
    print(LeetCode43(num1, num2))

    num1 = '978'
    num2 = '89'
    print(LeetCode43(num1, num2))

    num1 = '99'
    num2 = '88888'
    print(LeetCode43(num1, num2))

if __name__=='__main__':
    main()