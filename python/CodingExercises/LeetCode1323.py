'''
1323. Maximum 69 Number
Given a positive integer num consisting only of digits 6 and 9.
Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
Example 1:
Input: num = 9669
Output: 9969
Explanation:
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.
Example 2:
Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
Example 3:
Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
'''

def LeetCode1323(num):

    lst=list(str(num))
    output_lst=[]
    for i in range(0,len(lst)):
        key=lst[i]
        tmp=[]
        tmp.append(''.join(lst[:i]))
        if key=='9':
            tmp.append('6')
            if i<len(lst):
                tmp.append(''.join(lst[i+1:]))
        elif key=='6':
            tmp.append('9')
            if i < len(lst):
                tmp.append(''.join(lst[i + 1:]))

        output_lst.append(int(''.join(tmp)))
    if max(output_lst)>num:
        return max(output_lst)
    else:
        return num

def main():

    num=9669
    print(LeetCode1323(num))

    num = 9996
    print(LeetCode1323(num))

    num = 9999
    print(LeetCode1323(num))

if __name__=='__main__':
    main()