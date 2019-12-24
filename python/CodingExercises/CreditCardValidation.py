'''
Program for credit card number validation
Write a program that prompts the user to enter a credit card number as a long integer and Display whether that card is valid or invalid.
Credit card numbers follow certain patterns.
A credit card number must have between 13 and 16 digits. It must start with:
4 for Visa cards
5 for Master cards
37 for American Express cards
6 for Discover cards
The problem can be solved by using Luhn algorithm.
Luhn check or the Mod 10 check, which can be described as follows (for illustration,
consider the card number 4388576018402626):
Step 1. Double every second digit from right to left. If doubling of a digit results in a
two-digit number, add up the two digits to get a single-digit number (like for 12:1+2, 18=1+8).
Step 2. Now add all single-digit numbers from Step 1.
4 + 4 + 8 + 2 + 3 + 1 + 7 + 8 = 37
Step 3. Add all digits in the odd places from right to left in the card number.
6 + 6 + 0 + 8 + 0 + 7 + 8 + 3 = 38
Step 4. Sum the results from Step 2 and Step 3.
37 + 38 = 75
Step 5. If the result from Step 4 is divisible by 10, the card number is valid; otherwise, it is invalid.
Examples :
Input : 379354508162306
Output : 379354508162306 is Valid
Input : 4388576018402626
Output : 4388576018402626 is invalid
'''

def GetSum(number):
    sum=number
    while sum>9:
        temp=sum
        sum=0
        while temp!=0:
            rem=temp%10
            sum=sum+rem
            temp=temp//10
    return sum

def CreditCardValidation(num):

    credit=str(num)
    if len(credit)>=13 and len(credit)<=16:
        pass
    else:
        return 'InValid'

    if credit[0]=='4' or credit[0]=='5' or credit[0]=='6' or credit[:2]=='37':
        pass
    else:
        return 'InValid'
    k=1
    sum1=0
    sum2=0
    total_sum=0
    for i in range(len(credit)-1,-1,-1):
        if k%2==0:
            sum1=sum1+GetSum(2*int(credit[i]))
        else:
            sum2=sum2+int(credit[i])
        k=k+1
    total_sum=sum1+sum2
    if total_sum%10==0:
        return 'Valid'
    else:
        return 'InValid'

def main():

    num = 379354508162306
    print(CreditCardValidation(num))

    num = 4388576018402626
    print(CreditCardValidation(num))

if __name__=='__main__':
    main()