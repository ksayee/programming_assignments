'''
Remove recurring digits in a given number
Given a number as string, remove recurring digits from the given string.
The changes must be made in-place. Expected time complexity O(n) and auxiliary space O(1).
Examples:
Input:  num[] = "1299888833"
Output: num[] = "12983"
Input:  num[] = "1299888833222"
Output: num[] = "129832"
'''

def RemoveRecurringDigitsNumber(num):

    for i in range(0,len(num)):
        key=num[i]
        if i>0:
            if key in num[:i]:
                num=num[:i]+' '+num[i+1:]
    return ''.join(num).replace(' ','')


def main():
    
    num="1299888833"
    print(RemoveRecurringDigitsNumber(num))

    num = "1299888833222"
    print(RemoveRecurringDigitsNumber(num))

if __name__=='__main__':
    main()