'''
1118. Number of Days in a Month.
Easy
Given a year and month, return the number of days in that month and year.
Example 1:
Input: Y=1992, M=7
Output: 31
Example 2:
Input: Y=2000, M=2
Output: 29
Example 3:
Input: Y=1900, M=2
Output: 28
'''

def LeetCode1118(year,month):

    lst_month=[31,28,31,30,31,30,31,31,30,31,30,31]
    if year%4==0 and month==2:
        if year%100==0:
            if year%400==0:
                return 29
            else:
                return 28
        else:
            return 29
    return lst_month[month-1]

def main():

    year=1992
    month=7
    print(LeetCode1118(year,month))

    year = 2000
    month = 2
    print(LeetCode1118(year, month))

    year = 1900
    month = 2
    print(LeetCode1118(year, month))

if __name__=='__main__':
    main()