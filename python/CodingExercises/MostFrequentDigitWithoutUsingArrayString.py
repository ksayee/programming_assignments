'''
Find the most frequent digit without using array/string
Given an integer, find the most occurring digit in it.
If two or more digits occur same number of times,
then return the highest of them. Input integer is given as an int variable,
not as a string or array. Use of hash or array or string is not allowed.
Example:
Input:  x = 12234
Output: The most frequent digit is 2

Input:  x = 1223377
Output: The most frequent digit is 7

Input:  x = 5
Output: The most frequent digit is 5

Input:  x = 1000
Output: The most frequent digit is 0
'''

def FindDigitCount(num,key):

    count=0
    while num!=0:
        rem=num%10
        num=num//10
        if rem==key:
            count=count+1
    return count
def MostFrequentDigitWithoutUsingArrayString(num):

    maxDigit=-1
    maxCount=0
    for key in range(0,9):
        count=FindDigitCount(num,key)
        if count>maxCount:
            maxCount=count
            maxDigit=key
    return maxDigit

def main():
    
    num=12234
    print(MostFrequentDigitWithoutUsingArrayString(num))

    num = 1223377
    print(MostFrequentDigitWithoutUsingArrayString(num))

    num = 5
    print(MostFrequentDigitWithoutUsingArrayString(num))

    num = 1000
    print(MostFrequentDigitWithoutUsingArrayString(num))

if __name__=='__main__':
    main()